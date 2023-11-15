package main

import (
	"bytes"
	"errors"
	"flag"
	"fmt"
	"net"
	"net/http"
	"os"
	"strings"
)

type handlerFunc func(request *HttpRequest, directory string) string

var (
	getRoutes = map[string]handlerFunc{
		"/files/":     handleGetFile,
		"/echo/":      handleEcho,
		"/user-agent": handleUserAgent,
	}
	postRoutes = map[string]handlerFunc{
		"/files/": handlePostFile,
	}
)

type HttpRequest struct {
	Method    string
	Source    string
	UserAgent string
	Body      string
}

func (request *HttpRequest) SetRequest(rawRequest string) error {
	separator := "\r\n"
	data := strings.Split(rawRequest, separator)

	requestLine := strings.Split(data[0], " ")
	if len(requestLine) != 3 {
		return errors.New("error: First line should have 3 parameters")
	}
	request.Method = requestLine[0]
	request.Source = requestLine[1]

	headersLines := data[2:]
	request.Body = headersLines[len(headersLines)-1]
	for _, line := range headersLines {
		headerData := string(line)
		headerData = strings.TrimSpace(headerData)

		headerSplited := strings.Split(headerData, " ")
		if len(headerSplited) == 1 {
			continue
		}
		if len(headerSplited) != 2 {
			return errors.New("error: Header wrong format")
		}
		header := string(headerSplited[0])
		content := string(headerSplited[1])
		if header == "User-Agent:" {
			request.UserAgent = content
		}
	}

	fmt.Println(request)

	return nil
}

func (request *HttpRequest) String() string {
	var buffer bytes.Buffer
	buffer.WriteString(request.Method)
	buffer.WriteString(" ")
	buffer.WriteString(request.Source)
	buffer.WriteString(" ")
	buffer.WriteString(request.UserAgent)
	buffer.WriteString(" ")
	return buffer.String()
}

func (request *HttpRequest) processRouteRequest(directory string) string {
	var router map[string]handlerFunc
	if request.Method == http.MethodGet {
		router = getRoutes
	} else {
		router = postRoutes
	}

	for pathPrefix, handler := range router {
		if strings.HasPrefix(request.Source, pathPrefix) {
			return handler(request, directory)
		}
	}

	return "HTTP/1.1 404 Not Found\r\n\r\n"
}

func handleDefault(request *HttpRequest, directory string) string {
	return "HTTP/1.1 200 OK\r\n\r\n"
}

func handleEcho(request *HttpRequest, directory string) string {
	msg := strings.TrimPrefix(request.Source, "/echo/")
	return fmt.Sprintf("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: %v\r\n\r\n%v\r\n\r\n",
		len(msg), msg)
}

func handleUserAgent(request *HttpRequest, directory string) string {
	return fmt.Sprintf("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: %v\r\n\r\n%v\r\n\r\n",
		len(request.UserAgent), request.UserAgent)
}

func handlePostFile(request *HttpRequest, directory string) string {
	fileName := strings.TrimPrefix(request.Source, "/files/")
	filePath := fmt.Sprintf("%v%v", directory, fileName)

	file, err := os.Create(filePath)
	if err != nil {
		return "HTTP/1.1 500 Internal Server Error\r\n\r\n"
	}
	defer file.Close()

	_, err = file.WriteString(request.Body)
	if err != nil {
		return "HTTP/1.1 500 Internal Server Error\r\n\r\n"
	}

	file.Sync()

	return "HTTP/1.1 201 Created\r\n\r\n"
}

func handleGetFile(request *HttpRequest, directory string) string {
	fileName := strings.TrimPrefix(request.Source, "/files/")
	filePath := fmt.Sprintf("%v%v", directory, fileName)

	fmt.Println("The file path is: ", filePath)

	data, err := os.ReadFile(filePath)
	if err != nil {
		return "HTTP/1.1 404 Not Found\r\n\r\n"
	}

	return fmt.Sprintf("HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: %v\r\n\r\n%v\r\n\r\n",
		len(data), string(data))
}

func (request *HttpRequest) handleGetActions(directory string) string {
	if request.Source == "/" {
		return handleDefault(request, directory)
	}

	return request.processRouteRequest(directory)
}

func (request *HttpRequest) handlePostActions(directory string) string {
	return request.processRouteRequest(directory)
}

func handleConn(conn net.Conn, directory string) {
	defer conn.Close()

	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil {
		fmt.Println("Error while reading from the buffer", err.Error())
	}

	var request HttpRequest
	rawRequest := string(buffer[:n])
	request.SetRequest(rawRequest)

	var response string

	if request.Method == http.MethodGet {
		response = request.handleGetActions(directory)
	} else if request.Method == http.MethodPost {
		response = request.handlePostActions(directory)
	}

	conn.Write([]byte(response))
}

func main() {
	fmt.Println("Logs from your program will appear here!")

	directory := flag.String("directory", ".", "the directory you want")
	flag.Parse()

	l, err := net.Listen("tcp", "0.0.0.0:4221")
	if err != nil {
		fmt.Println("Failed to bind to port 4221")
		os.Exit(1)
	}

	for {
		conn, err := l.Accept()
		if err != nil {
			fmt.Println("Error accepting connection: ", err.Error())
			os.Exit(1)
		}

		go handleConn(conn, *directory)
	}
}
