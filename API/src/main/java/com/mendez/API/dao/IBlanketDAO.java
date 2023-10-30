package com.mendez.API.dao;

import com.mendez.API.models.Blanket;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface IBlanketDAO extends JpaRepository<Blanket, Long> {
	List<Blanket> findByType(String type);
	
	List<Blanket> findByWidthCM(int widthCM);
	
	List<Blanket> findByHeightCM(int heightCM);
}
