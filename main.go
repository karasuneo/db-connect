package main

import (
	"log"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)
  
  func main() {
	dsn := "root:Z,YqLuaw/Nu0@tcp(localhost:3306)/test?charset=utf8mb4&parseTime=True&loc=Local"
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal(err)
	}

	print(db)
  }
