package com.mendez.API.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;

@Entity
@Table(name = "blankets")
public class Blanket implements Comparable<Blanket>, Serializable {
	
	@Id
	@GeneratedValue(strategy =  GenerationType.IDENTITY)
	@Getter
	private Long id;
	
	@Column
	@Getter
	@Setter
	private String type;
	
	@Column
	@Getter
	@Setter
	private int widthCM;
	
	@Column
	@Getter
	@Setter
	private int heightCM;
	
	private int area(){
		return widthCM*heightCM;
	}
	
	@Override
	public int compareTo(Blanket o) {
		return this.area() - o.area();
	}
}
