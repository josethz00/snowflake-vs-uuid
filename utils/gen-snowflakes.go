package utils

import "github.com/bwmarrin/snowflake"

func GenSnowflake(node *snowflake.Node) int64 {
	generatedSnowflake := node.Generate().Int64()
	return generatedSnowflake
}
