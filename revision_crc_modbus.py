def revisar_is_crc(list_buffer_editado):
	try:
		CRC = 0xFFFF
		j = 0
		i = 0
		flagy = 0

		list_temp = list_buffer_editado[0:-2]

		for j in list_temp:
			CRC = CRC ^ j
			contador = 8
			while contador > 0:
				contador -= 1
				flagy = CRC & 0x0001
				CRC = ( CRC >> 1 ) & 0x7FFF
				if( flagy == 0x0001 ):
					CRC = CRC ^ 0xA001

		crc_hi = int(CRC / 0x100)
		crc_lo = int(CRC & 0xFF)

		if((list_buffer_editado[-2] == crc_lo) and (list_buffer_editado[-1] == crc_hi)):
			print("CRC Correcto")
		else:
			print("CRC Incorrecto, el crc correcto es: {}-{}".format(crc_lo, crc_hi))
	except Exception as e:
		print('exception - revisar_is_crc - {}'.format(e))

def entregar_crc(lista_crc):
	try:
		CRC = 0xFFFF
		j = 0
		i = 0
		flagy = 0

		for x in range(len(lista_crc)) :
			lista_crc[x] = int(lista_crc[x])

		for j in lista_crc:
			CRC = CRC ^ j
			contador = 8
			while contador > 0:
				contador -= 1
				flagy = CRC & 0x0001
				CRC = ( CRC >> 1 ) & 0x7FFF
				if( flagy == 0x0001 ):
					CRC = CRC ^ 0xA001
		return CRC
	except Exception as e:
		print('exception - entregar_crc - {}'.format(e))

lista_temp = [1, 3, 0x1b, 0x59, 0, 1, 0x52, 0xfd]

revisar_is_crc(lista_temp)