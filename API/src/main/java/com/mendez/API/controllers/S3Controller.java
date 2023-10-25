package com.mendez.API.controllers;

import com.mendez.API.services.IS3Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/s3")
public class S3Controller {
	@Autowired
	private IS3Service ss;
	
	// Load information as a file to S3 and as data to RDS
	@PostMapping("/upload/{fileName}")
	public ResponseEntity<String> uploadFile(@RequestParam(value = "file") MultipartFile file, @PathVariable String fileName){
		return new ResponseEntity<>(ss.uploadFile(file, fileName), HttpStatus.CREATED);
	}
	
	@GetMapping("/download/{fileName}")
	public ResponseEntity<ByteArrayResource> downloadFile(@PathVariable String fileName){
		byte[] data = ss.downloadFile(fileName);
		ByteArrayResource resource = new ByteArrayResource(data);
		return ResponseEntity
				.ok()
				.contentLength(data.length)
				.header("Content-type", "application/octet-stream")
				.header("Content-disposition", "attachment; filename=\"" + fileName + "\"")
				.body(resource);
	}
	
	@GetMapping("/fileCount")
	public ResponseEntity<String> fileCount(){
		return new ResponseEntity<>("En el bucket existen " + ss.fileCount() + " archivos", HttpStatus.OK);
	}
}
