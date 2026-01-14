package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"time"
)

type Company struct {
	AltPhoneNumber            string    `json:"altPhoneNumber"`
	CompanyName               string    `json:"companyName"`
	CompanyRegistrationDate   time.Time `json:"companyRegistrationDate"`
	CompanyRegistrationNumber string    `json:"companyRegistrationNumber"`
	CustomerType              string    `json:"customerType"`
	Email                     string    `json:"email"`
	InstitutionID             string    `json:"institutionId"`
	Introducer                string    `json:"introducer"`
	Location                  string    `json:"location"`
	PhoneNumber               string    `json:"phoneNumber"`
	RelationshipOfficerID     string    `json:"relationshipOfficerId"`
	TinNumber                 string    `json:"tinNumber"`
}

const apiUrl = "https://gims-broker-backend-main.onrender.com/api/v1/customers/active/companies"
const bearerToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwMTliYjAxNy1mNzkxLTc5NjItODkwOS05Mjg4YjFmODQ5ZWMiLCJleHAiOjE3Njg0MzA4MjMsImlhdCI6MTc2ODQyMDAyMywidXNlcklkIjoiMDE5YmIwMTctZjc5MS03OTYyLTg5MDktOTI4OGIxZjg0OWVjIiwiZW1haWwiOiJuaWlAbWFpbC5jb20iLCJmaXJzdE5hbWUiOiJOaWkiLCJsYXN0TmFtZSI6Ik5paSIsImxhc3RMb2dnZWRJbkF0IjoiMjAyNi0wMS0xMlQwOTozMDozNi41NDc1MDMwNzZaIn0.OxoJNYlcXig49lJ8b0jI_BEpsxqa6AR0f0u7-RHfclc"

func main() {

	ticker := time.NewTicker(1200 * time.Millisecond)
	done := make(chan bool)
	// open the json file
	file, err := os.ReadFile("individual_customers_output.json")

	if err != nil {
		log.Fatalf("error reading file: %s", err.Error())

	}

	// defer closing the file to prevent memory leaks

	var companies []Company

	// create a JSON decoder for the file
	if err != json.Unmarshal(file, &companies) {
		log.Fatalf("error when unmarshaling json: %v", err)
	}

	// iterate to submit
	for index, company := range companies {

		data, err := json.Marshal(company)
		if err != nil {
			log.Fatalf("error marshaling json data: %v", err)
		}

		req, _ := http.NewRequest(http.MethodPost, apiUrl, bytes.NewBuffer(data))
		req.Header.Add("Content-Type", "application/json")
		req.Header.Add("Authorization", bearerToken)

		response, err := http.DefaultClient.Do(req)
		if err != nil {
			log.Fatalf("error sending post request number %d: %v", index+1, err)
		}

		defer response.Body.Close()

		if response.StatusCode == http.StatusOK || response.StatusCode == http.StatusAccepted {
			fmt.Printf("Success: Created %d: %s\n", index+1, company.CompanyName)
		} else {
			fmt.Printf("Failed: %d. Status = %d\n", index+1, response.StatusCode)
		}

		body, _ := io.ReadAll(response.Body)

		fmt.Println(string(body))

		select {
		case <-done:
			continue
		case t := <-ticker.C:
			fmt.Printf("Done at: %v\n", t)
		}
	}

	ticker.Stop()
	done <- true

	fmt.Println("All requests sent")
}
