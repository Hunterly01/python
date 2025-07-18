Menu = """
	1-> Phonebook
	2-> Messages
	3-> Chat
	4-> Call register
	5-> Tones
	6-> Settings
	7-> Call divert
	8-> Games
	9-> Calculator
	10-> Reminder
	11-> Clock
	12-> Profiles
	13-> SIM services 
"""
print(Menu)
Menu_option = int(input("Enter a option:"))
match Menu_option:
	case 1:
		Phonebook = """
			phonebook
			1-> Search
			2-> Service Nos
			3-> Add name
			4-> Erase
			5-> Edit
			6-> Assign tone
			7-> Send b'card
			8-> 0ption
			9-> Speed dials
			10-> voice tags
		"""
		print(Phonebook)
		Phonebook_option = int(input("Enter a option:"))
		match Phonebook_option:
			case 1: 
				print("1-> Search")
			case 2:
				print("2-> Service Nos")
			case 3:
				print("3-> Add name")
			case 4:
				print("4-> Erase")
			case 5: 
				print("5-> Edit")
			case 6:
				print("6-> Assign tone")
			case 7:
				print("7-> Send b'card")
			case 8:
				print("8-> 0ption")
				Option = """
				1-> Type of view
				2-> Memory status
				"""
				print(Option)
				Option_option = int(input("Enter a option:"))
				match Option_option:
					case 1:
						print("1-> Type of view") 
					case 2:
						print("2-> Memory status")
					case _: 
						print("Invalid input")


			case 9:
				print("9-> Speed dials")
			case 10:
				print("10-> voice tags")
			case _: 
				print("Invalid input")

	

	

	case 2:
		
		messages = """ 
		 	Messages
		1-> Write messages
		2-> Inbox
		3-> Outbox
		4-> Picture messages
		6-> Smileys
		5-> Template
		7-> Message settings
		8-> Info service
		9-> Voice mailbox number
		10-> Service command editor
		"""
		print(messages)
		messages_option = int(input("Enter a option:"))
		match messages_option: 
			case 1: 
				print("1-> Write messages")
			case 2:
				print("2-> Inbox")
			case 3:
				print("3-> Outbox")
			case 4:
				print("4-> Picture messages")
			case 5:
				print("5-> Template")
			case 6:
				print("6-> Smileys")
			case 7:
				Message_settings = """
				1-> Set
				2-> Common
				"""
				print(Message_settings)
				Message_settings_option = int(input("Enter a option:"))
				match Message_settings_option:
					case 1:
						Set = """
						1-> Message centre number
						2-> Messages sent as
						3-> Message validity
						"""
						print(Set)
						Set_option = int(input("Enter a option:"))
						match Set_option:
							case 1: 
								print("1-> Message centre number")
							case 2:
								print("2-> Messages sent as")
							case 3:
								print("3-> Message validity")
							case _:
								print("Invalid input")
						
						
					case 2:
						Common = """
						1-> Delivery reports
						2-> Reply via same centre
						3-> Character support
						"""
						print(Common)
						Common_option = int(input("Enter a option:"))
						match Common_option:
							case 1: 
								print("1-> Delivery reports")
							case 2:
								print("2-> Reply via same centre")
							case 3:
								print("3-> Character support")
							case _:
								print("Invalid input")					

					case _: 
						print("Invalid input")

			case 8:
				print("8-> Info service")
			case 9:
				print("9-> Voice mailbox number")
			case 10:
				print("10-> Service command editor")
			case _: 
				print("Invalid input")
					

				
				
	

	case 3:
		print("3-> Chat")
	case 4:
		call_register = """
			call register
			1-> Missed calls
			2-> Received calls 
			3-> Dialled calls
			4-> Erase recent call list
			5-> Show call duration
			6-> Show call costs
			7-> Call cost settings
			8-> Prepaid credit
			"""
		print(call_register)
		call_register_option = int(input("Enter a option:"))
		match call_register_option:
			case 1: 
				print("1-> Missed calls")
			case 2:
				print("2-> Received calls")
			case 3:
				print("3-> Dialled calls")
			case 4:
				print("4-> Erase recent call list")
			case 5: 
				show_call_duration = """
				1-> Last call duration
				2-> All calls duration
				3-> Received calls duration
				4-> Dialled calls duration
				5-> Clear times
				"""
				print(show_call_duration)
				show_call_duration_option = int(input("Enter a option:"))
				match show_call_duration_option:
					case 1:
						print("1-> Last call duration") 
					case 2:
						print("2-> All calls duration")
					case 3:
						print("3-> Received calls duration")
					case 4:
						print("4-> Dialled calls duration")
					case 5:
						print("5-> Clear times")
					case _: 
						print("Invalid input")
			


			case 6:
				show_call_costs = """
				1-> Last call cost
				2-> All calls cost
				3-> clear counters
				"""
				print(show_call_costs)
				show_call_costs_option = int(input("Enter a option:"))
				match show_call_costs_option:
					case 1:
						print("1-> Last call cost") 
					case 2:
						print("2-> All calls cost")
					case 3:
						print("3-> clear counters")
					case _: 
						print("Invalid input")
			

			case 7:
				call_cost_settings = """
				1-> Last call cost
				2-> All calls cost
				"""
				print(call_cost_settings)
				call_cost_settings_option = int(input("Enter a option:"))
				match call_cost_settings_option:
					case 1:
						print("1-> Last call cost") 
					case 2:
						print("2-> All calls cost")
					case _: 
						print("Invalid input")


	

			case 8:
				print("8-> Prepaid credit")
			case _:
				print("Invalid input")
	case 5:
		Tones = """
			Tones
			1-> Ringing tone
			2-> Ringing volume
			3-> Incoming call
			4-> Composer
			5-> Message alert tone
			6-> Keypad tones
			7-> Warning and game tones
			8-> Vibrating
			9-> Screen saver
			"""
		print(Tones)
		Tones_option = int(input("Enter a option:"))
		match Tones_option:
			case 1: 
				print("1-> Ringing tone")
			case 2:
				print("2-> Ringing volume")
			case 3:
				print("3-> Incoming call")
			case 4:
				print("4-> Composer")
			case 5: 
				print("5-> Message alert tone")
			case 6:
				print("6-> Keypad tone")
			case 7:
				print("7-> Warning and game tones")
			case 8:
				print("8-> Vibrating")
			case 9:
				print("9-> Screen saver")
			case _:
				print("Invalid input")
	

	case 6:
		print("6-> Settings")
		settings = """
			Settings
			1-> Call settings
			2-> Phone settings
			2-> Security settings
			4-> Restore factory settings
			"""
		print(settings)
		settings_option = int(input("Enter a option:"))
		match settings_option:
			case 1: 
				call_settings = """
				1-> Automatic redial
				2-> Speed dialing
				3-> Call waiting option
				4-> own number sending
				5-> Phone in use 
				6-> Automatic answer
				"""
				print(call_settings)
				call_settings_option = int(input("Enter a option:"))
				match call_settings_option:
					case 1:
						print("1-> Automatic redial") 
					case 2:
						print("2-> Speed dialing")
					case 3:
						print("3-> Call waiting option")
					case 4:
						print("4-> own number sending")
					case 5:
						print("5-> Phone in use")
					case 6:
						print("6-> Automatic answer")
					case _: 
						print("Invalid input")

			case 2:
				
				phone_settings = """
				1-> Language
				2-> Cell info
				3-> Welcome note
				4-> Network  selection
				5-> Lights
				6-> Confirm SIM service actions
				"""
				print(phone_settings)
				phone_settings_option = int(input("Enter a option:"))
				match phone_settings_option:
					case 1:
						print("1-> Language") 
					case 2:
						print("2-> Cell info")
					case 3:
						print("3-> Welcome note")
					case 4:
						print("4-> Network  selection")
					case 5:
						print("5-> Lights")
					case 6:
						print("6-> Confirm SIM service actions")
					case _: 
						print("Invalid input")


			case 3:
				
				security_settings = """
				1-> PIN code request
				2-> Call barring service
				3-> Fixed dialing
				4-> Closed user group
				5-> Phone security
				6-> Change access codes
				"""
				print(security_settings)
				security_settings_option = int(input("Enter a option:"))
				match security_settings_option:
					case 1:
						print("1-> PIN code request") 
					case 2:
						print("2-> Call barring service")
					case 3:
						print("3-> Fixed dialing")
					case 4:
						print("4-> Closed user group")
					case 5:
						print("5-> Phone security")
					case 6:
						print("6-> Change access codes")
					case _: 
						print("Invalid input")




			case 4:
				print("4-> Restore factory settings")
			case _:
				print("Invalid input")


		
	case 7:
		print("7-> Call divert")
	case 8:
		print("8-> Games")
	case 9:
		print("9-> Calculator")
	case 10:
		print("10-> Reminder")
	case 11:
		
		clock = """
			clock
			1-> Alarm clock
			2-> Clock settings
			3-> Date setting
			4-> Stopwatch
			5-> Countdown timer
			6-> Auto update of date and time
			"""
		print(clock)
		clock_option = int(input("Enter a option:"))
		match clock_option:
			case 1: 
				print("1-> Alarm clock")
			case 2:
				print("2-> Clock settings")
			case 3:
				print("3-> Date setting")
			case 4:
				print("4-> Stopwatch")
			case 5: 
				print("5-> Countdown timer")
			case 6:
				print("6-> Auto update of date and time")
			case _:
				print("Invalid input")

	case 12:
		print("12-> Profiles")
	case 13:
		print("13-> SIM services ")
	case _: 
		print("invalid iput")