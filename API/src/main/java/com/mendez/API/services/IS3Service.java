package com.mendez.API.services;

import org.springframework.web.multipart.MultipartFile;

public interface IS3Service {
	String uploadFile(MultipartFile file, String fileName);
	
	byte[] downloadFile(String fileName);
	
	long fileCount();
}
