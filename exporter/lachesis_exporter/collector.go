package main

import (
	"bytes"
	"encoding/json"
	"net/http"
	"strconv"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
)

// TODO: Heavy Refactor!
var currentEpoch = promauto.NewGauge(prometheus.GaugeOpts{
	Name: "current_epoch", Help: "Current epoch number"})

var url = "http://localhost:18545"

type EpochResponseBody struct {
	JSONRPC string `json:"jsonrpc"`
	ID      int64  `json:"id"`
	Result  string `json:"result"`
}

type EpochRequestBody struct {
	JSONRPC string `json:"jsonrpc"`
	Method  string `json:"method"`
	ID      int64  `json:"id"`
}

func getCurrentEpoch() int64 {
	header := "application/json"
	body, _ := json.Marshal(&EpochRequestBody{
		JSONRPC: "2.0",
		Method:  "ftm_currentEpoch",
		ID:      1,
	})

	response, err := http.Post(url, header, bytes.NewBuffer(body))
	if err != nil {
		panic(err)
	} else {
		var data EpochResponseBody
		err := json.NewDecoder(response.Body).Decode(&data)
		if err != nil {
			panic(err)
		}
		epoch, _ := strconv.ParseInt(data.Result, 0, 64)
		return epoch
	}
}

// RecordMetrics | Update all metrics
func RecordMetrics() {
	go func() {
		for {
			currentEpoch.Set(float64(getCurrentEpoch()))
			time.Sleep(2 * time.Second)
		}
	}()
}
