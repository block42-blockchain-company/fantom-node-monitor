package main

import (
	"net/http"

	log "github.com/Sirupsen/logrus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	RecordMetrics()

	http.Handle("/metrics", promhttp.Handler())
	log.Info("Beginning to serve on port :9777")
	log.Fatal(http.ListenAndServe(":9777", nil))

}
