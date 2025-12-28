package main

import (
	"fmt"
	"time"
)

func main() {
	for {
		fmt.Println("[Collector] Collecting logs...")
		time.Sleep(2 * time.Second)
	}
}
