package utils

import (
	"github.com/jmoiron/sqlx"
)

type DB struct {
	*sqlx.DB
}

func NewDB() *DB {
	return &DB{}
}

func (db *DB) ConnectDB() *DB {
	dbconn, err := sqlx.Connect("postgres", "user=postgres-benchmark dbname=postgres-benchmark password=postgres-benchmark host=localhost port=5571 sslmode=disable")
	if err != nil {
		panic(err)
	}

	db = &DB{dbconn}
	return db
}

func (db *DB) InsertIntoTestsUUID(id string, name string) error {
	_, err := db.Exec("INSERT INTO tests_uuid(id, name) VALUES ($1, $2)", id, name)
	if err != nil {
		return err
	}
	return nil
}

func (db *DB) InsertIntoTestsSnowflake(id int64, name string) error {
	_, err := db.Exec("INSERT INTO tests_snowflake(id, name) VALUES ($1, $2)", id, name)
	if err != nil {
		return err
	}
	return nil
}
