// Package api provides primitives to interact with the openapi HTTP API.
//
// Code generated by github.com/deepmap/oapi-codegen version v1.12.4 DO NOT EDIT.
package api

// ReportData defines model for ReportData.
type ReportData struct {
	Author    string                  `json:"author"`
	Body      string                  `json:"body"`
	Course    int                     `json:"course"`
	Group     string                  `json:"group"`
	LabNumber string                  `json:"labNumber"`
	Static    *map[string]interface{} `json:"static,omitempty"`
	Teacher   string                  `json:"teacher"`
	Title     string                  `json:"title"`
	WorkType  string                  `json:"workType"`
}

// GenerateReportJSONRequestBody defines body for GenerateReport for application/json ContentType.
type GenerateReportJSONRequestBody = ReportData
