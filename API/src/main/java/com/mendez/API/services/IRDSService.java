package com.mendez.API.services;

import com.mendez.API.models.Blanket;

import java.util.List;

public interface IRDSService {
	
	Blanket save(Blanket blanket);
	
	Blanket findById(Long id);
	
	List<Blanket> findAll();
	
	void deleteById(Long id);
	
	List<Blanket> findByType(String type);
	
	List<Blanket> findByWidthCM(int widthCM);
	
	List<Blanket> findByHeightCM(int heightCM);
}
