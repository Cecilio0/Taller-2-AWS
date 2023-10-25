package com.mendez.API.services;

import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.model.*;
import com.amazonaws.util.IOUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

@Service
@Slf4j
public class S3Service implements IS3Service{
	@Value("${application.bucket.name}")
	private String bucketName;
	
	@Autowired
	private AmazonS3 s3Client;
	
	@Override
	public String uploadFile(MultipartFile file, String fileName){
		File fileObj = convertMultiPartFileToFile(file);
		s3Client.putObject(new PutObjectRequest(bucketName, fileName, fileObj));
		fileObj.delete();
		return "File uploaded :)";
	}
	
	@Override
	public byte[] downloadFile(String fileName){
		S3Object s3Object = s3Client.getObject(bucketName, fileName);
		S3ObjectInputStream inputStream = s3Object.getObjectContent();
		try{
			return IOUtils.toByteArray(inputStream);
		} catch (IOException e){
			e.printStackTrace();
		}
		return null;
	}
	
	@Override
	public long fileCount(){
		ObjectListing list = s3Client.listObjects(bucketName);
		return list.getObjectSummaries().size();
	}
	
	private File convertMultiPartFileToFile(MultipartFile file){
		File convertedFile = new File(file.getOriginalFilename());
		try (FileOutputStream fos = new FileOutputStream(convertedFile)){
			fos.write(file.getBytes());
		} catch(IOException e){
			log.error("Error converting multipartFile to file", e);
		}
		return convertedFile;
	}
}
