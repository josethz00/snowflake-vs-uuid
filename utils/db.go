package utils

import (
	"time"

	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

type DB struct {
	*sqlx.DB
}

type TestsUUID struct {
	ID        string    `db:"id"`
	Name      string    `db:"name"`
	CreatedAt time.Time `db:"created_at"`
	UpdatedAt time.Time `db:"updated_at"`
}

type TestsSnowflake struct {
	ID        int64     `db:"id"`
	Name      string    `db:"name"`
	CreatedAt time.Time `db:"created_at"`
	UpdatedAt time.Time `db:"updated_at"`
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

func (db *DB) TruncateTestsSnowflakeTable() error {
	_, err := db.Exec("TRUNCATE TABLE tests_snowflake")
	if err != nil {
		return err
	}
	return nil
}

func (db *DB) TruncateTestsUUIDTable() error {
	_, err := db.Exec("TRUNCATE TABLE tests_uuid")
	if err != nil {
		return err
	}
	return nil
}

func (db *DB) SelectIdFromTestsSnowflake() ([]int64, error) {
	results := []int64{}
	err := db.Select(&results, "SELECT id FROM tests_snowflake")

	if err != nil {
		return nil, err
	}

	return results, nil
}

func (db *DB) SelectIdFromTestsUUID() ([]string, error) {
	results := []string{}

	err := db.Select(&results, "SELECT id FROM tests_uuid")

	if err != nil {
		return nil, err
	}

	return results, nil
}

func (db *DB) SearchBySnowflake(snowflakeId int64) (TestsSnowflake, error) {
	results := TestsSnowflake{}

	err := db.Get(&results, "SELECT * FROM tests_snowflake WHERE id = $1", snowflakeId)

	if err != nil {
		return TestsSnowflake{}, err
	}

	return results, nil
}

func (db *DB) SearchByUUID(uuid_ string) (TestsUUID, error) {
	results := TestsUUID{}

	err := db.Get(&results, "SELECT * FROM tests_uuid WHERE id = $1", uuid_)

	if err != nil {
		return TestsUUID{}, err
	}

	return results, nil
}
