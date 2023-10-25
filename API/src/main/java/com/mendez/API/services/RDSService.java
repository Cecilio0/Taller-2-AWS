package com.mendez.API.services;

import com.mendez.API.dao.IBlanketDAO;
import com.mendez.API.models.Blanket;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RDSService implements IRDSService{
	@Autowired
	private IBlanketDAO blanketDAO;
	
	@Override
	public Blanket save(Blanket blanket) {
		return blanketDAO.save(blanket);
	}
	
	@Override
	public Blanket findById(Long id) {
		return blanketDAO.findById(id).orElse(null);
	}
	
	@Override
	public List<Blanket> findAll() {
		return blanketDAO.findAll();
	}
	
	@Override
	public void deleteById(Long id) {
		blanketDAO.deleteById(id);
	}
}
