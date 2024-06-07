import streamlit as st
import pandas as pd
import numpy as np
import time

def initial_data():
    jarak = np.array([[0, 6, 0, 7, 10, 8, 11, 0, 12, 0, 7, 0, 9], 
                       [6, 0, 2, 0, 3, 0, 3, 4, 7, 8, 0, 1, 3], 
                       [0, 3, 0, 4, 1, 0, 1, 2, 0, 5, 4, 3, 2], 
                       [7, 3, 4, 0, 4, 3, 0, 5, 6, 7, 0, 3, 4],
                       [9, 3, 1, 0, 0, 3, 1, 2, 0, 5, 3, 2, 0], 
                       [9, 2, 3, 0, 3, 0, 4, 5, 4, 5, 0, 0, 1], 
                       [10, 0, 1, 5, 1, 3, 0, 1, 3, 4, 3, 0, 2], 
                       [11, 4, 2, 0, 0, 4, 1, 0, 4, 5, 4, 3, 3], 
                       [13, 6, 4, 7, 0, 5, 3, 4, 0, 1, 6, 5, 4], 
                       [12, 7, 2, 0, 3, 4, 0, 0, 0, 0, 4, 4, 3], 
                       [7, 1, 9, 3, 2, 1, 2, 0, 6, 7, 0, 1 ,2], 
                       [8, 2, 3, 2 ,0, 1, 4, 5, 4, 5, 2, 0, 1], 
                       [9, 2, 2, 0, 2, 1, 0, 4, 4, 0, 2, 1, 0]])
    #st.title(jarak[0,4])
    return jarak

def template(angka):
	if angka == 2:
		jarak = np.array([[0, 0], 
                    	   [0, 0]])
	if angka == 3:
		jarak = np.array([[0, 0, 0], 
                    	   [0, 0, 0], 
                    	   [0, 0, 0]])
	if angka == 4:
		jarak = np.array([[0, 0, 0, 0], 
                    	   [0, 0, 0, 0], 
                    	   [0, 0, 0, 0], 
                    	   [0, 0, 0, 0]])
	if angka == 5:
		jarak = np.array([[0, 0, 0, 0, 0], 
        	               [0, 0, 0, 0, 0], 
            	           [0, 0, 0, 0, 0], 
                	       [0, 0, 0, 0, 0],
                    	   [0, 0, 0, 0, 0]])
	if angka == 6:
		jarak = np.array([[0, 0, 0, 0, 0, 0], 
        	               [0, 0, 0, 0, 0, 0], 
            	           [0, 0, 0, 0, 0, 0], 
                	       [0, 0, 0, 0, 0, 0],
                    	   [0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0]])
	if angka == 7:
		jarak = np.array([[0, 0, 0, 0, 0, 0, 0], 
        	               [0, 0, 0, 0, 0, 0, 0], 
            	           [0, 0, 0, 0, 0, 0, 0], 
                	       [0, 0, 0, 0, 0, 0, 0],
                    	   [0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0]])
	if angka == 8:
		jarak = np.array([[0, 0, 0, 0, 0, 0, 0, 0], 
        	               [0, 0, 0, 0, 0, 0, 0, 0], 
            	           [0, 0, 0, 0, 0, 0, 0, 0], 
                	       [0, 0, 0, 0, 0, 0, 0, 0],
                    	   [0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0]])
	if angka == 9:
		jarak = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        	               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            	           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                	       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    	   [0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0]])
	if angka == 10:
		jarak = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        	               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            	           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                	       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
	return jarak


# def template1():
#     jarak = np.array([[0, 0, 0, 0], 
#                        [0, 0, 0, 0], 
#                        [0, 0, 0, 0], 
#                        [0, 0, 0, 0]])
#     return jarak

# def template2():
#     jarak = np.array([[0, 0, 0, 0, 0], 
#                        [0, 0, 0, 0, 0], 
#                        [0, 0, 0, 0, 0], 
#                        [0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0]])
#     return jarak

	
def pencarian_indeks(data):
	listCodeTempat = ["User","A1","A2","A3","A4","B1","B2","C1","D1","D2","E1","E2","E3"]
	found = -1
	i = 0
	while (i < 13 and found == -1) :
		if listCodeTempat[i] == data:
			found = i
		i += 1
	return found

def enkripsi(data):
	if data == "Bomber Burger" or data == "1":
		return "A1"
	elif data == "Drunk Baker" or data == "2":
		return "A2"
	elif data == "Ayam Goreng Gorowok Asep Tiyen" or data == "3":
		return "A3"
	elif data == " San Gimignano" or data == "4":
		return "A4"
	elif data == "Alun-Alun" or data == "5":
		return "B1"
	elif data == "Lapangan Gasibu" or data == "6":
		return "B2"
	elif data == "Museum Geologi" or data == "7":
		return "C1"
	elif data == "PVJ Mall" or data == "8":
		return "D1"
	elif data == "Ciwalk" or data == "9":
		return "D2"
	elif data == "The Hallway Space" or data == "10":
		return "E1"
	elif data == "Jalan Asia-Afrika" or data == "11":
		return "E2"
	elif data == "Jalan Braga" or data == "12":
		return "E3"
	elif data == "0":
		return "User"

def kategori(x):
	if x[0] == "A":
		data = listKategoriKuliner(x)
	elif x[0] == "B":
		data = listKategoriTaman(x)
	elif x[0] == "C":
		data = listKategoriMuseum(x)
	elif x[0] == "D":
		data = listKategoriMall(x)
	elif x[0] == "E":
		data = listKategoriLainnya(x)
	else:
		data = "Saya"
	return data


def listKategoriKuliner(x):
	if x[1] == "1":
		return ("Bomber Burger")
	elif x[1] == "2":
		return("Drunk Baker")
	elif x[1] == "3":
		return("Ayam Goreng Gorowok Asep Tiyen")
	elif x[1] == "4":
		return("San Gimignano (Gelato, coffee & kitchen)")
	
def listKategoriTaman(x):
	if x[1] == "1":
		return("Alun-alun Bandung")
	elif x[1] == "2":
		return("Lapangan Gasibu")

def listKategoriMuseum(x):
	if x[1] == "1":
		return("Museum Geologi")

def listKategoriMall(x):
	if x[1] == "1":
		return("Paris Van Java")
	elif x[1] == "2":
		return("Ciwalk")

def listKategoriLainnya(x):
	if x[1] == "1":
		return("The Hallway Space")
	elif x[1] == "2":
		return("Jalan Asia-Afrika")
	elif x[1] == "3":
		return("Jalan Braga")


def permutation(lst):

	# If lst is empty then there are no permutations
	if len(lst) == 0:
		return []

	# If there is only one element in lst then, only
	# one permutation is possible
	if len(lst) == 1:
		return [lst]

	# Find the permutations for lst if there are
	# more than 1 characters

	l = [] # empty list that will store current permutation

	# Iterate the input(lst) and calculate the permutation
	for i in range(len(lst)):
		m = lst[i]

		# Extract lst[i] or m from the list. remLst is
		# remaining list
		remLst = lst[:i] + lst[i+1:]


	# Generating all permutations where m is first
	# element
		for p in permutation(remLst):
			l.append([m] + p)
	return l


def bruteForce (n, tempat, jarak):
	i = 0
	data = ""
	while i <= n:
		data += str(i)
		i += 1
	
	for i in range(13):
		for j in range(13):
			if jarak[i,j] == 0 and i != j:
				jarak[i,j] = 9999
	
	min = 9999
	data = list(data)
	Hasil_brute_force = []
	KotaMin = "NULL"
	p = permutation(data)
	for p in permutation(data):
		total = 0
		kota = ""
		for i in range (n):
			data = tempat[int(p[i])]
			x = pencarian_indeks(data)
			kota += p[i]
			data = tempat[int(p[i+1])]
			y = pencarian_indeks(data)
			total += jarak[x, y]
		data = tempat[int(p[i+1])]
		x = pencarian_indeks(data)
		kota += p[i+1]
		data = tempat[int(p[0])]
		y = pencarian_indeks(data)
		kota += p[0]
		total += jarak[x, y]

		if total < min:
			min = total
			KotaMin = kota
		Hasil_brute_force.append (total)
	return Hasil_brute_force, min, KotaMin

def TSP_DP(graph, v, currPos, n, count, cost, path, min_cost, min_path):
 
    
    if count == n and graph[currPos][0]:
        if cost + graph[currPos][0] < min_cost[0]:
            min_cost[0] = cost + graph[currPos][0]
            min_path[0] = path[:] + [0]  # Tambahkan simpul awal untuk menyelesaikan siklus
        return
 
    # BACKTRACKING STEP
    # Perulangan untuk melintasi daftar kedekatan
	# dari simpul currPos dan meningkatkan hitungan
	# dengan 1 dan biaya dengan nilai graph[currPos][i]
    for i in range(n):
        if not v[i] and graph[currPos][i]:
            # Mark as visited
            v[i] = True
            # Append the current node to the path
            path.append(i)
            TSP_DP(graph, v, i, n, count + 1, cost + graph[currPos][i], path, min_cost, min_path)
            # Mark ith node as unvisited
            v[i] = False
            # Remove the last node from the path
            path.pop()

# Display logo and title
st.image("Locatrip_removebg.png", width=700)  # Adjust width as needed
st.title("Mau Ke Mana nih?")

# Navigation menu items (replace with your actual pages)
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "Tempat yang tersimpan"])

# Display content based on selected page
if page == "Home":
    st.write("Pilih banyak tempat tujuan:")
    option = st.selectbox("Select:", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    count = 0

    tempat = ["User"]
    for i in range (int(option)):
        temp = (st.selectbox("Select:", ["Pilih tujuan", "Bomber Burger", "Drunk Baker", "Ayam Goreng Gorowok Asep Tiyen", " San Gimignano", "Alun-Alun", "Lapangan Gasibu", "Museum Geologi", "PVJ Mall", "Ciwalk", "The Hallway Space", "Jalan Asia-Afrika", "Jalan Braga"], key = count))
        temp = enkripsi(temp)
        tempat.append (temp)
        count += 1

    #for i in range(int(option)+1):
    #    st.title(tempat[i])
	
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Brute Force TSP'):
            st.session_state.algorithm = "Brute Force"
            st.session_state.criterion = None
    with col2:
        if st.button('Dynamic Programming TSP'):
            st.session_state.algorithm = "DP"
            st.session_state.criterion = None

if st.session_state.algorithm == "Brute Force":
	if st.button('Hitung Solusi'):
		if st.session_state.algorithm == "Brute Force":
			start_time = time.time()
			jarak = initial_data()
			array, minimum, kota12 = bruteForce(int(option), tempat, jarak)
			if kota12 != "NULL":
				temp = list(kota12)
				tujuan = ""
				for i in range(int(option)+1):
					sementara = tempat[int(temp[i])]
					tujuan += kategori(sementara)
					tujuan += " -> "
			else:
				tujuan = kota12

			st.title("TSP By Bruteforce")

			st.subheader("Hasil Rute Perjalanan")
			st.write(f"{tujuan}")

			st.subheader("Jarak Rute")
			st.write(f"{minimum}")

			st.subheader("")
			st.subheader("Running Time")
			end_time = time.time()
			execution_time = (end_time-start_time)
			st.write(f"{execution_time} detik")

elif st.session_state.algorithm == "DP":
	if st.button('Hitung Solusi'):
		start_time = time.time()
		jarak = initial_data()
		for i in range(13):
			for j in range(13):
				if jarak[i,j] == 0 and i != j:
					jarak[i,j] = 9999
		newJarak = template(int(option)+1)
		temporary = []
		for i in range (len(tempat)):
			data = enkripsi(tempat[i])
			temporary.append (pencarian_indeks(tempat[i]))
		for i in range (len(tempat)):
			for j in range (len(tempat)):
				newJarak[i,j] = jarak[temporary[i],temporary[j]]

		n = len(newJarak)
		visited = [False] * n
		visited[0] = True  # Start from node 0
		answer = []  # To store the minimum cost
		path = [0]    # Start with node 0
		min_cost = [float('inf')]  # To store the minimum cost found so far
		min_path = [[]]  # To store the minimum path found so far
		TSP_DP(newJarak, visited, 0, n, 1, 0, path, min_cost, min_path)
		data = list(min_path[0])


		#if data != "NULL":
		# if min_cost[0] > 9999:
		# 	st.title("Hasil: Null")
		# 	st.title("Jarak: Null")
		# else:
		tujuan = ""
		for i in range(int(option)+1):
			sementara = tempat[int(data[i])]
			tujuan += kategori(sementara)
			tujuan += " -> "
		#st.title(min_path[0])

		st.title("TSP By Dynamic Programming")

		st.subheader("Hasil Rute Perjalanan")
		st.write(f"{tujuan}")

		st.subheader("Jarak Rute")
		st.write(f"{min_cost[0]}")
	
		st.subheader("")
		st.subheader("Running Time")
		end_time = time.time()
		execution_time = (end_time-start_time)
		st.write(f"{execution_time} detik")
		#st.title(hasil)