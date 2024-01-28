package utils

import (
	"github.com/google/uuid"
)

func GenUUID() string {
	generatedUUID := uuid.New()
	return generatedUUID.String()
}
