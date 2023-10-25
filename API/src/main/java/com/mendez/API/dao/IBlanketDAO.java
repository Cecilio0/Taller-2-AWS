package com.mendez.API.dao;

import com.mendez.API.models.Blanket;
import org.springframework.data.jpa.repository.JpaRepository;

public interface IBlanketDAO extends JpaRepository<Blanket, Long> {
}
