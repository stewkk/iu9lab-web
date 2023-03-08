package api

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

type ServerInterfaceImpl struct {}

func (handler *ServerInterfaceImpl) GenerateReport(ctx echo.Context) error {
	return nil
}


func (handler *ServerInterfaceImpl) Ping(ctx echo.Context) error {
	return ctx.NoContent(http.StatusOK)
}
