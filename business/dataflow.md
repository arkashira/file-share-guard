# dataflow.md

## External Data Sources
External data sources for file-share-guard include:

* User-uploaded files via the web interface
* File system integration (e.g. local file uploads)
* API integrations (e.g. SFTP, FTP)

## Ingestion Layer
The ingestion layer is responsible for receiving and processing incoming data from external sources.

* **File Receiver**: Responsible for receiving and storing user-uploaded files
	+ Components:
		- File upload handler (e.g. Express.js)
		- File storage (e.g. local file system, S3)
* **File System Integrator**: Responsible for integrating with local file systems
	+ Components:
		- File system watcher (e.g. inotify)
		- File storage (e.g. local file system, S3)
* **API Integrator**: Responsible for integrating with external APIs (e.g. SFTP, FTP)
	+ Components:
		- API client (e.g. `sftp-client`)
		- File storage (e.g. local file system, S3)

## Processing/Transform Layer
The processing/transform layer is responsible for processing and transforming incoming data.

* **File Processor**: Responsible for processing and transforming uploaded files
	+ Components:
		- File metadata extractor (e.g. `file-metadata`)
		- File encryption/decryption (e.g. `crypto-js`)
* **Link Expiration Manager**: Responsible for managing link expiration
	+ Components:
		- Link expiration timer (e.g. `node-schedule`)
		- Link database (e.g. Redis)

## Storage Tier
The storage tier is responsible for storing processed data.

* **File Storage**: Responsible for storing uploaded files
	+ Components:
		- Local file system storage (e.g. `fs`)
		- S3 storage (e.g. `aws-sdk`)
* **Link Database**: Responsible for storing link metadata
	+ Components:
		- Redis database (e.g. `redis`)
		- Link expiration timer (e.g. `node-schedule`)

## Query/Serving Layer
The query/serving layer is responsible for serving data to users.

* **API Server**: Responsible for serving API requests
	+ Components:
		- API router (e.g. Express.js)
		- API client (e.g. `sftp-client`)
* **Web Interface**: Responsible for serving web requests
	+ Components:
		- Web framework (e.g. React)
		- File metadata extractor (e.g. `file-metadata`)

## Egress to User
The egress to user layer is responsible for serving data to users.

* **File Download**: Responsible for serving downloaded files
	+ Components:
		- File server (e.g. `http-server`)
		- File encryption/decryption (e.g. `crypto-js`)
* **Link Serving**: Responsible for serving links
	+ Components:
		- Link database (e.g. Redis)
		- Link expiration timer (e.g. `node-schedule`)

## Auth Boundaries
Auth boundaries are implemented at the following points:

* **File Upload**: Authentication required for file uploads
* **API Access**: Authentication required for API access
* **Link Serving**: Authentication required for link serving

### ASCII Block Diagram
```
+---------------+
|  External    |
|  Data Sources  |
+---------------+
       |
       |
       v
+---------------+
|  Ingestion    |
|  Layer        |
+---------------+
|  File Receiver  |
|  File System    |
|  Integrator    |
|  API Integrator |
+---------------+
       |
       |
       v
+---------------+
|  Processing/  |
|  Transform Layer|
+---------------+
|  File Processor  |
|  Link Expiration |
|  Manager        |
+---------------+
       |
       |
       v
+---------------+
|  Storage Tier  |
+---------------+
|  File Storage  |
|  Link Database  |
+---------------+
       |
       |
       v
+---------------+
|  Query/Serving  |
|  Layer          |
+---------------+
|  API Server     |
|  Web Interface  |
+---------------+
       |
       |
       v
+---------------+
|  Egress to User  |
+---------------+
|  File Download  |
|  Link Serving    |
+---------------+
```
Note: This is a high-level architecture diagram and may not include all components or details.