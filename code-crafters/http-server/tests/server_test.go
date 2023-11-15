package main

import (
	"bytes"
	"net"
	"testing"
)

const serverAddr = ":4221"

func TestEchoService(t *testing.T) {
	var tests = []struct {
		name             string
		request          []byte
		expectedResponse []byte
	}{
		{
			"echo service 1",
			[]byte("GET /echo/abc HTTP/1.1\r\n\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\n"),
			[]byte("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 3\r\n\r\nabc\r\n\r\n"),
		},
		{
			"echo service 2",
			[]byte("GET /echo/Twice/Momo HTTP/1.1\r\n\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\n"),
			[]byte("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 10\r\n\r\nTwice/Momo\r\n\r\n"),
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			conn, err := net.Dial("tcp", serverAddr)
			if err != nil {
				t.Errorf("Failed to connect to server: %v", err)
			}
			defer conn.Close()

			if _, err := conn.Write(tt.request); err != nil {
				t.Errorf("Failed to send the request: %v", err)
			}

			response := make([]byte, 1024)
			n, err := conn.Read(response)
			if err != nil {
				t.Errorf("Failed to read the response: %v", err)
			}

			if !bytes.Equal(response[:n], tt.expectedResponse) {
				t.Errorf("Response does not match expected. Got: %v, expected: %v", string(response[:n]), string(tt.expectedResponse))
			}

		})
	}
}

func TestUserAgentService(t *testing.T) {
	var tests = []struct {
		name             string
		request          []byte
		expectedResponse []byte
	}{
		{
			"User-Agent Service: 1",
			[]byte("GET /user-agent HTTP/1.1\r\n\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\n"),
			[]byte("HTTP/1.1 200 OK\r\n\r\nContent-Type: text/plain\r\nContent-Length: 11\r\n\r\ncurl/7.64.1\r\n\r\n"),
		},
		// {
		// 	"echo service 2",
		// 	[]byte("GET /echo/Twice/Momo HTTP/1.1\r\n\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\n"),
		// 	[]byte("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 10\r\n\r\nTwice/Momo\r\n\r\n"),
		// },
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			conn, err := net.Dial("tcp", serverAddr)
			if err != nil {
				t.Errorf("Failed to connect to server: %v", err)
			}
			defer conn.Close()

			if _, err := conn.Write(tt.request); err != nil {
				t.Errorf("Failed to send the request: %v", err)
			}

			response := make([]byte, 1024)
			n, err := conn.Read(response)
			if err != nil {
				t.Errorf("Failed to read the response: %v", err)
			}

			if !bytes.Equal(response[:n], tt.expectedResponse) {
				t.Errorf("Response does not match expected. \nGot: %v \nexpected: %v", string(response[:n]), string(tt.expectedResponse))
			}

		})
	}
}
