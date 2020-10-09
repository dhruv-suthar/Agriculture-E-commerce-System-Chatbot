

class Secure_Data:
	string = "klabcdefghiszyx"
	
	@classmethod
	def decrypt(cls,mo_bo,otp):
		
		dc_mobo=""
		dc_otp=""
		i=0
		while i<len(mo_bo):
			dc_mobo += str(cls.string.find(mo_bo[i]))
			i+=1

		i=0	
		while i<len(otp):
			dc_otp+=str(cls.string.find(otp[i]))
			i+=1
					
		return dc_mobo,dc_otp	


	@classmethod	
	def encrypt(cls,mo_bo,otp):
		en_mobo=""
		en_otp=""

		i=0
		while i<len(mo_bo):
			en_mobo += cls.string[int(mo_bo[i])]
			i+=1

		i=0
		while i<len(otp):
			en_otp += cls.string[int(otp[i])]
			i+=1	

			
		return en_mobo,en_otp








		
