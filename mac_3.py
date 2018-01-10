##########################
###
###
###  Lecture 3, Macine Learning
###
###
###
##########################





##Example from project


os.chdir("/Users/justingrimmer/Dropbox/Women in Committees/106th Congress (1999 - 2000)/House Hearings")

dirs = os.listdir(os.getcwd())

comms = open('/Users/justingrimmer/Dropbox/Women in Committees/Justin/Attendance.csv', 'w')
comms.write('Committee,Title,Member,State')
comms.write('\n')




for z in dirs:
	os.chdir("/Users/justingrimmer/Dropbox/Women in Committees/106th Congress (1999 - 2000)/House Hearings" + '/' + z)
	files = os.listdir(os.getcwd())
	for y in range(len(files)):
		title = re.sub('.txt', '', re.sub('\s+', ' ', re.sub('\W', ' ', files[y])))
		text = open(files[y], 'r').readlines()
		for m in range(len(text)):
			ert = re.findall('U.S. GOVERNMENT PRINTING OFFICE', text[m])
			if len(ert)>0:
				a = 0
				iter = m 
				while a ==0:
					iter+=1 
					finds = re.findall('[A-Z].+[A-Z],\s[A-Z][a-z]+?\s[A-Z][a-z]+', text[iter])
					if len(finds)>0:
						splits = re.split('\s\s+',finds[0])
						if len(splits)>0:
							for x in splits:
								second = x.split(',')
								if len(second)>1:
									name = second[0].lower().strip('\n')
									state = second[1].lower().strip('\n')
									comms.write('%s,%s,%s,%s' %(z,title, name,state))
									comms.write('\n')
					staff = re.findall('Staff', text[iter])
					if len(staff)>0 or iter == (len(text) - 1):
						a = 1
	print z








	