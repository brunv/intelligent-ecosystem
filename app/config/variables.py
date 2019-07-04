# antelope_num 				=> number of agents initially
# initial_health : 50		=> health when agent borns
# born_chance : 2 			=> 80% chance to agent born
# min_health_breeding : 50 	=> 50 life points is the minimum life to agent breed
# food_refill :50			=> food regenerates 50 health points
# water_refill : 10			=> water regenerates 50 health points
# damage_points : 5 		=> life points decrease 5 in each step
# damage_chance : 5 		=> 50% chance to decrease life points in each step
antelope_variables = {"antelope_num" : 20,
					"initial_health" : 100, 
					"born_chance" : 1,
					"min_health_breeding" : 10,
					"food_refill" : 50,
					"water_refill" : 10,
					"damage_points" : 5,
					"damage_chance" : 5}

bird_variables = {"bird_num" : 15,
				"initial_health" : 100, 
				"born_chance" : 1,
				"min_health_breeding" : 10,
				"food_refill" : 50,
				"water_refill" : 10,
				"damage_points" : 2,
				"damage_chance" : 5}

crocodile_variables = {"crocodile_num": 8,
					"initial_health" : 100, 
					"born_chance" : 1,
					"min_health_breeding" : 10,
					"food_refill" : 50,
					"damage_points" : 4,
					"damage_chance" : 7}

lion_variables = {"lion_num": 5,
				"initial_health" : 150, 
				"born_chance" : 1,
				"min_health_breeding" : 10,
				"food_refill" : 20,
				"water_refill" : 10,
				"damage_points" : 4,
				"damage_chance" : 7}

snake_variables = {"snake_num" : 5,
				"initial_health" : 100, 
				"born_chance" : 1,
				"min_health_breeding" : 10,
				"food_refill" : 50,
				"water_refill" : 10,
				"damage_points" : 3,
				"damage_chance" : 5}

bush_variables = {"bush_num" : 90}