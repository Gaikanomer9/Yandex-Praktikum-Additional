FROM golang:1.14.3-alpine AS builder

WORKDIR /src

COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o /go/bin/main

FROM scratch

COPY --from=builder /go/bin/main /go/bin/main

# COPY index.html /static/

ENTRYPOINT ["/go/bin/main"]