package com.mendez.API.services;

import com.mendez.API.models.Blanket;

import java.util.List;

public interface IRDSService {
	
	public Blanket save(Blanket blanket);
	
	public Blanket findById(Long id);
	
	public List<Blanket> findAll();
	
	public void deleteById(Long id);
	
}
