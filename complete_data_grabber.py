###########################################################
###                   Infobright 2011                   ###
###            Developed by: Infobright Intern Team     ###
###                 Author: Infobright Intern Team      ###
###                     Version 1.0                     ###
###                                                     ###
### v1.0: Infobright Intern Team                        ###
###                                                     ###
### The MIT License                                     ###
###                                                     ###
### Copyright (c) 2011 Infobright Inc.                  ###
###                                                     ###
### Permission is hereby granted, free of charge, to    ###
### any person obtaining a copy of this software and    ###
### associated documentation files (the "Software"), to ###
### deal in the Software without restriction, including ###
### without limitation the rights to use, copy, modify, ###
### merge, publish, distribute, sublicense, and/or sell ###
### copies of the Software, and to permit persons to    ###
### whom the Software is furnished to do so, subject to ###
### the following conditions:                           ###
###                                                     ###
### The above copyright notice and this permission      ###
### notice shall be included in all copies or           ###
### substantial portions of the Software.               ###
###                                                     ###
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY  ###
### OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT  ###
### LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       ###
### FITNESS FOR A PARTICULAR PURPOSE AND NON-           ###
### INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR      ###
### COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES  ###
### OR OTHER LIABILITY, WHETHER IN AN ACTION OF         ###
### CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF   ###
### OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR    ###
### OTHER DEALINGS IN THE SOFTWARE.                     ###
##########################################################h
# Description                                            #h
#                                                        #h
#   This script grabs data from the MillionSong tables   #h
#   and generates a flat file that contains              #h
#   data that will be used to populate the               #h
#   Complete table.                                      #h
#                                                        #h
# Assumption(s):                                         #h
# - numpy, tables, numexpr and python are installed      #h
# - installed with default location for server script    #h
#                                                        #h
# Caveats:                                               #h
# - tested only on 32/64 bit CentOS and Ubuntu           #h
#                                                        #h
##########################################################h
# Usage                                                  #h
#                                                        #h
# <path>/python complete_data_grabber.py                 #h
#                                                        #h
##########################################################h

import os
import glob
import csv
import hdf5_getters
import numpy
import array
import genre_dict
import string
import time

def get_avg(array):
	""" Return the average of an array. """
        size=len(array)
	if size != 0:
		average= numpy.average(array)
		return average	
	else:
		return 0

def get_max(array):
	""" Return the maximum number in an array. """
	size=len(array)
	if size != 0:
		max=numpy.amax(array)
		return max
	else:
		return 0

def get_min(array):
	""" Return the minimum number in an array. """
	size=len(array)
	if size != 0:
		min=numpy.amin(array)
		return min
	else:
		return 0
	

def get_count(array):
	""" Return the number of elements in an array. """
	size=len(array)
	if size != 0:
		count= len(array)
		return count
	else:
		return 0


def get_sum(array):
	""" Return the total sum of the elements in the array. """
	size=len(array)
	if size != 0:
		summy = numpy.sum(array)
		return summy
	else:
		return 0


def get_stddev(array):
	""" Return the standard deviation of the elements in the array. """
	size=len(array)
	if size != 0:
		stddev = numpy.std(array)
		return stddev
	else:
		return 0

		

def get_genre_indexes(array):
	""" Return the biggest 10 frequencies in the array. """
	ind = numpy.argsort(array)
	rev = ind[::-1]
	indexes=rev[0:10]
	return indexes

def get_genre(array,index):
	"""Return the element that corresponds to that index in the array. """
	return array[index]

def is_number(s):
	""" Returns True/False depending if the input is a number or not. """
	try:
		float(s)
		return True
	except ValueError:
		return False



def genre_columns(array):
	""" Return the genre_array, each element of the array corresponds to a genre. Therefore it will contain a 1 if that genre corresponds to the song and 0 otherwise """
	genre_array=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0']
	if array == -1:
		return genre_array
	else:

		for index in range(len(array)):
			array[index]=array[index]-1

		for i in range(len(genre_array)):
			for index in array:
				if i == index:
					genre_array[i]='1'

		return genre_array





         #files = glob.glob(os.path.join(root,'TRAIIUE128E07826EC.h5'))
	 #files = glob.glob(os.path.join(root,'*'+ext))


def padding(blanks):
	"""Return an array with blank spaces """
	row=[""] * blanks
	return row




def data_to_flat_file(basedir,ext='.h5') :
    """ This function extracts the information from the tables and creates the flat file. """
    count = 0; #song counter
    list_to_write= []
    group_index=0
    row_to_write = ""
    writer = csv.writer(open("complete.csv", "wb"))
    for root, dirs, files in os.walk(basedir):
	files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
	    row=[]
	    print f
            h5 = hdf5_getters.open_h5_file_read(f)
	    title = hdf5_getters.get_title(h5) 
	    title= title.replace('"','') 
            row.append(title)
	    comma=title.find(',')
	    if	comma != -1:
		    print title
		    time.sleep(1)
	    album = hdf5_getters.get_release(h5)
	    album= album.replace('"','')
            row.append(album)
	    comma=album.find(',')
	    if	comma != -1:
		    print album
		    time.sleep(1)
	    artist_name = hdf5_getters.get_artist_name(h5)
	    comma=artist_name.find(',')
	    if	comma != -1:
		    print artist_name
		    time.sleep(1)
	    artist_name= artist_name.replace('"','')
            row.append(artist_name)
	    duration = hdf5_getters.get_duration(h5)
            row.append(duration)
	    samp_rt = hdf5_getters.get_analysis_sample_rate(h5)
            row.append(samp_rt)
	    artist_7digitalid = hdf5_getters.get_artist_7digitalid(h5)
            row.append(artist_7digitalid)
	    artist_fam = hdf5_getters.get_artist_familiarity(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(artist_fam) == True:
	            artist_fam=-1
            row.append(artist_fam)
	    artist_hotness= hdf5_getters.get_artist_hotttnesss(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(artist_hotness) == True:
	             artist_hotness=-1
            row.append(artist_hotness)
	    artist_id = hdf5_getters.get_artist_id(h5)
            row.append(artist_id)           
	    artist_lat = hdf5_getters.get_artist_latitude(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(artist_lat) == True:
	            artist_lat=-1
            row.append(artist_lat)
	    artist_loc = hdf5_getters.get_artist_location(h5)
            row.append(artist_loc)
	    artist_lon = hdf5_getters.get_artist_longitude(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(artist_lon) == True:
	            artist_lon=-1
            row.append(artist_lon)
	    artist_mbid = hdf5_getters.get_artist_mbid(h5)
            row.append(artist_mbid)

	    #Getting the genre				       
            art_trm = hdf5_getters.get_artist_terms(h5)
            trm_freq = hdf5_getters.get_artist_terms_freq(h5)
	    trn_wght = hdf5_getters.get_artist_terms_weight(h5)
	    a_mb_tags = hdf5_getters.get_artist_mbtags(h5)
	    genre_indexes=get_genre_indexes(trm_freq) 		    #index of the highest freq
	    genre_set=0					            #flag to see if the genre has been set or not
	    final_genre=[]
	    genres_so_far=[]
	    for i in range(len(genre_indexes)):
		    genre_tmp=get_genre(art_trm,genre_indexes[i])   #genre that corresponds to the highest freq
		    genres_so_far=genre_dict.get_genre_in_dict(genre_tmp) #getting the genre from the dictionary
		    if len(genres_so_far) != 0:
			for i in genres_so_far:
				final_genre.append(i)
			    	genre_set=1
			
			
	    if genre_set == 1:
		col_num=[]
		for i in final_genre:
			column=int(i)				#getting the column number of the genre
			col_num.append(column)
	
		genre_array=genre_columns(col_num)	                #genre array 
	        for i in range(len(genre_array)):                   	#appending the genre_array to the row 
			row.append(genre_array[i])
	    else:
		genre_array=genre_columns(-1)				#when there is no genre matched, return an array of [0...0]
	        for i in range(len(genre_array)):                   	#appending the genre_array to the row 
			row.append(genre_array[i])
					

	    artist_pmid = hdf5_getters.get_artist_playmeid(h5)
            row.append(artist_pmid)
	    audio_md5 = hdf5_getters.get_audio_md5(h5)
            row.append(audio_md5)
	    danceability = hdf5_getters.get_danceability(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(danceability) == True:
	            danceability=-1
            row.append(danceability)
	    end_fade_in =hdf5_getters.get_end_of_fade_in(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(end_fade_in) == True:
	            end_fade_in=-1
            row.append(end_fade_in)
	    energy = hdf5_getters.get_energy(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(energy) == True:
	            energy=-1
            row.append(energy)
            song_key = hdf5_getters.get_key(h5)
            row.append(song_key)
	    key_c = hdf5_getters.get_key_confidence(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(key_c) == True:
	            key_c=-1
            row.append(key_c)
	    loudness = hdf5_getters.get_loudness(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(loudness) == True:
	            loudness=-1
            row.append(loudness)
	    mode = hdf5_getters.get_mode(h5)
            row.append(mode)
	    mode_conf = hdf5_getters.get_mode_confidence(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(mode_conf) == True:
	            mode_conf=-1
            row.append(mode_conf)
	    release_7digitalid = hdf5_getters.get_release_7digitalid(h5)
            row.append(release_7digitalid)
	    song_hot = hdf5_getters.get_song_hotttnesss(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(song_hot) == True:
	            song_hot=-1
            row.append(song_hot)
	    song_id = hdf5_getters.get_song_id(h5)
            row.append(song_id)
	    start_fade_out = hdf5_getters.get_start_of_fade_out(h5)
            row.append(start_fade_out)
	    tempo = hdf5_getters.get_tempo(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(tempo) == True:
	            tempo=-1
            row.append(tempo)
	    time_sig = hdf5_getters.get_time_signature(h5)
            row.append(time_sig)
	    time_sig_c = hdf5_getters.get_time_signature_confidence(h5)
	    #checking if we get a "nan" if we do we change it to -1
	    if numpy.isnan(time_sig_c) == True:
	            time_sig_c=-1
            row.append(time_sig_c)
	    track_id = hdf5_getters.get_track_id(h5)
            row.append(track_id)
	    track_7digitalid = hdf5_getters.get_track_7digitalid(h5)
            row.append(track_7digitalid)
	    year = hdf5_getters.get_year(h5)
            row.append(year)
	    bars_c = hdf5_getters.get_bars_confidence(h5)
            bars_start = hdf5_getters.get_bars_start(h5)
	    row_bars_padding=padding(245)   #this is the array that will be attached at the end of th row

	    #--------------bars---------------"
	    gral_info=[]
	    gral_info=row[:]
	    empty=[]
	    for i,item in enumerate(bars_c):
                row.append(group_index)
                row.append(i)
                row.append(bars_c[i])
	        bars_c_avg= get_avg(bars_c)
                row.append(bars_c_avg)
	        bars_c_max= get_max(bars_c)	
                row.append(bars_c_max)
	        bars_c_min = get_min(bars_c)
                row.append(bars_c_min)
	        bars_c_stddev= get_stddev(bars_c)
                row.append(bars_c_stddev)
	        bars_c_count = get_count(bars_c)
                row.append(bars_c_count)
	        bars_c_sum = get_sum(bars_c)
                row.append(bars_c_sum)
                row.append(bars_start[i])	         
	        bars_start_avg = get_avg(bars_start)
                row.append(bars_start_avg)	         
	        bars_start_max= get_max(bars_start)
                row.append(bars_start_max)	         
	        bars_start_min = get_min(bars_start)
                row.append(bars_start_min)	         
	        bars_start_stddev= get_stddev(bars_start)
                row.append(bars_start_stddev)	         
	        bars_start_count = get_count(bars_start)
                row.append(bars_start_count)	         
	        bars_start_sum = get_sum(bars_start)
                row.append(bars_start_sum)	         
		for i in row_bars_padding:
			row.append(i)

                writer.writerow(row)
		row=[]
		row=gral_info[:]
	 

            #--------beats---------------"
	    beats_c = hdf5_getters.get_beats_confidence(h5)
	    group_index=1
	    row=[]
	    row=gral_info[:]
	    row_front=padding(14)  	#blanks left in front of the row(empty spaces for bars)
	    row_beats_padding=padding(231)
	    for i,item in enumerate(beats_c):
	   	row.append(group_index)
		row.append(i)
		for index in row_front:  #padding blanks in front of the beats
			row.append(index)
		
		row.append(beats_c[i])
	        beats_c_avg= get_avg(beats_c)
		row.append(beats_c_avg)
	        beats_c_max= get_max(beats_c)
		row.append(beats_c_max)
                beats_c_min = get_min(beats_c)
		row.append(beats_c_min)
	        beats_c_stddev= get_stddev(beats_c)
		row.append(beats_c_stddev)
	        beats_c_count = get_count(beats_c)
		row.append(beats_c_count)
	        beats_c_sum = get_sum(beats_c)
		row.append(beats_c_sum)
                beats_start = hdf5_getters.get_beats_start(h5)
		row.append(beats_start[i])
 	        beats_start_avg = get_avg(beats_start)
		row.append(beats_start_avg)
	        beats_start_max= get_max(beats_start)
		row.append(beats_start_max)
	        beats_start_min = get_min(beats_start)
		row.append(beats_start_min)
	        beats_start_stddev= get_stddev(beats_start)
		row.append(beats_start_stddev)
	        beats_start_count = get_count(beats_start)
		row.append(beats_start_count)
	        beats_start_sum = get_sum(beats_start)
		row.append(beats_start_sum)
		for i in row_beats_padding:
			row.append(i)
                
		writer.writerow(row)
		row=[]
		row=gral_info[:]

            # "--------sections---------------"
	    row_sec_padding=padding(217)	#blank spaces left at the end of the row
	    sec_c = hdf5_getters.get_sections_confidence(h5)
	    group_index=2
	    row=[]
	    row=gral_info[:]
	    row_front=padding(28)		#blank spaces left in front(empty spaces for bars,beats)
	    for i,item in enumerate(sec_c):
		row.append(group_index)
		row.append(i)
		for index in row_front:  	#padding blanks in front of the sections
			row.append(index)

		row.append(sec_c[i])
                sec_c_avg= get_avg(sec_c)
		row.append(sec_c_avg)
	        sec_c_max= get_max(sec_c)
		row.append(sec_c_max)
	        sec_c_min = get_min(sec_c)
		row.append(sec_c_min)
	        sec_c_stddev= get_stddev(sec_c)
		row.append(sec_c_stddev)
	        sec_c_count = get_count(sec_c)
		row.append(sec_c_count)
	        sec_c_sum = get_sum(sec_c)
		row.append(sec_c_sum)
	        sec_start = hdf5_getters.get_sections_start(h5)
		row.append(sec_start[i])	   
                sec_start_avg = get_avg(sec_start)
		row.append(sec_start_avg)
	        sec_start_max= get_max(sec_start)
		row.append(sec_start_max)
	        sec_start_min = get_min(sec_start)
		row.append(sec_start_min)
	        sec_start_stddev= get_stddev(sec_start)
		row.append(sec_start_stddev)
	        sec_start_count = get_count(sec_start)
		row.append(sec_start_count)
	        sec_start_sum = get_sum(sec_start)
		row.append(sec_start_sum)
		for i in row_sec_padding:	#appending the blank spaces at the end of the row
			row.append(i)
                

		writer.writerow(row)
		row=[]
		row=gral_info[:]


            #--------segments---------------"
	    row_seg_padding=padding(182)	#blank spaces at the end of the row
 	    row_front=padding(42)		#blank spaces left in front of segments
	    seg_c = hdf5_getters.get_segments_confidence(h5)
	    group_index=3
	    row=[]
	    row=gral_info[:]
	    for i,item in enumerate(seg_c):
		row.append(group_index)
		row.append(i)
		for index in row_front:  	#padding blanks in front of the segments
			row.append(index)

		row.append(seg_c[i])
                seg_c_avg= get_avg(seg_c)
		row.append(seg_c_avg)
	        seg_c_max= get_max(seg_c)
		row.append(seg_c_max)
	        seg_c_min = get_min(seg_c)
		row.append(seg_c_min)
	        seg_c_stddev= get_stddev(seg_c)
		row.append(seg_c_stddev)
	        seg_c_count = get_count(seg_c)
		row.append(seg_c_count)
	        seg_c_sum = get_sum(seg_c)
		row.append(seg_c_sum)
                seg_loud_max = hdf5_getters.get_segments_loudness_max(h5)
		row.append(seg_loud_max[i])
                seg_loud_max_avg= get_avg(seg_loud_max)
		row.append(seg_loud_max_avg)
	        seg_loud_max_max= get_max(seg_loud_max)
		row.append(seg_loud_max_max)
	        seg_loud_max_min = get_min(seg_loud_max)
		row.append(seg_loud_max_min)
	        seg_loud_max_stddev= get_stddev(seg_loud_max)
		row.append(seg_loud_max_stddev)
	        seg_loud_max_count = get_count(seg_loud_max)
		row.append(seg_loud_max_count)
	        seg_loud_max_sum = get_sum(seg_loud_max)
		row.append(seg_loud_max_sum)
	        seg_loud_max_time = hdf5_getters.get_segments_loudness_max_time(h5)
		row.append(seg_loud_max_time[i])
	        seg_loud_max_time_avg= get_avg(seg_loud_max_time)
		row.append(seg_loud_max_time_avg)
	        seg_loud_max_time_max= get_max(seg_loud_max_time)
		row.append(seg_loud_max_time_max)
	        seg_loud_max_time_min = get_min(seg_loud_max_time)
		row.append(seg_loud_max_time_min)
	        seg_loud_max_time_stddev= get_stddev(seg_loud_max_time)
		row.append(seg_loud_max_time_stddev)
	        seg_loud_max_time_count = get_count(seg_loud_max_time)
		row.append(seg_loud_max_time_count)
	        seg_loud_max_time_sum = get_sum(seg_loud_max_time)
		row.append(seg_loud_max_time_sum)
	        seg_loud_start = hdf5_getters.get_segments_loudness_start(h5)
		row.append(seg_loud_start[i])
	        seg_loud_start_avg= get_avg(seg_loud_start)
		row.append(seg_loud_start_avg)
	        seg_loud_start_max= get_max(seg_loud_start)
		row.append(seg_loud_start_max)
	        seg_loud_start_min = get_min(seg_loud_start)
		row.append(seg_loud_start_min)
	        seg_loud_start_stddev= get_stddev(seg_loud_start)
		row.append(seg_loud_start_stddev)
	        seg_loud_start_count = get_count(seg_loud_start)
		row.append(seg_loud_start_count)
	        seg_loud_start_sum = get_sum(seg_loud_start)					      
		row.append(seg_loud_start_sum)
	        seg_start = hdf5_getters.get_segments_start(h5)
		row.append(seg_start[i])
	        seg_start_avg= get_avg(seg_start)
		row.append(seg_start_avg)
	        seg_start_max= get_max(seg_start)
		row.append(seg_start_max)
	        seg_start_min = get_min(seg_start)
		row.append(seg_start_min)
	        seg_start_stddev= get_stddev(seg_start)
		row.append(seg_start_stddev)
	        seg_start_count = get_count(seg_start)
		row.append(seg_start_count)
	        seg_start_sum = get_sum(seg_start)
		row.append(seg_start_sum)
		for i in row_seg_padding:	#appending blank spaces at the end of the row
			row.append(i)
                
		writer.writerow(row)
		row=[]
		row=gral_info[:]

	    #----------segments pitch and timbre---------------"
	    row_seg2_padding=padding(14)	#blank spaces left at the end of the row
	    row_front=padding(77)		#blank spaces left at the front of the segments and timbre
	    seg_pitch = hdf5_getters.get_segments_pitches(h5)
	    transpose_pitch= seg_pitch.transpose()          #this is to tranpose the matrix,so we can have 12 rows
	    group_index=4
	    row=[]
	    row=gral_info[:]
	    for i,item in enumerate(transpose_pitch[0]):
		row.append(group_index)
		row.append(i)
		for index in row_front:  	#padding blanks in front of segments and timbre
			row.append(index)
	   
		row.append(transpose_pitch[0][i])
  		seg_pitch_avg= get_avg(transpose_pitch[0])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[0])	
		row.append(seg_pitch_max)
		seg_pitch_min = get_min(transpose_pitch[0])
		row.append(seg_pitch_min)
		seg_pitch_stddev= get_stddev(transpose_pitch[0])
		row.append(seg_pitch_stddev)
		seg_pitch_count = get_count(transpose_pitch[0])
		row.append(seg_pitch_count)
		seg_pitch_sum = get_sum(transpose_pitch[0])
		row.append(seg_pitch_sum)   
 		row.append(transpose_pitch[1][i])
 		seg_pitch_avg= get_avg(transpose_pitch[1])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[1])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[1])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[1])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[1])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[1])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[2][i])
 		seg_pitch_avg= get_avg(transpose_pitch[2])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[2])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[2])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[2])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[2])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[2])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[3][i])
 		seg_pitch_avg= get_avg(transpose_pitch[3])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[3])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[3])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[3])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[3])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[3])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[4][i])
 		seg_pitch_avg= get_avg(transpose_pitch[4])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[4])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[4])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[4])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[4])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[4])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[5][i])
 		seg_pitch_avg= get_avg(transpose_pitch[5])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[5])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[5])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[5])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[5])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[5])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[6][i])
 		seg_pitch_avg= get_avg(transpose_pitch[6])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[6])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[6])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[6])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[6])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[6])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[7][i])
 		seg_pitch_avg= get_avg(transpose_pitch[7])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[7])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[7])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[7])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[7])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[7])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[8][i])
 		seg_pitch_avg= get_avg(transpose_pitch[8])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[8])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[8])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[8])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[8])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[8])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[9][i])
 		seg_pitch_avg= get_avg(transpose_pitch[9])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[9])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[9])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[9])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[9])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[9])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[10][i])
 		seg_pitch_avg= get_avg(transpose_pitch[10])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[10])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[10])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[10])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[10])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[10])
		row.append(seg_pitch_sum)   
		row.append(transpose_pitch[11][i])
 		seg_pitch_avg= get_avg(transpose_pitch[11])
		row.append(seg_pitch_avg)
		seg_pitch_max= get_max(transpose_pitch[11])	
		row.append(seg_pitch_max)
	        seg_pitch_min = get_min(transpose_pitch[11])
		row.append(seg_pitch_min)
	        seg_pitch_stddev= get_stddev(transpose_pitch[11])
		row.append(seg_pitch_stddev)
	        seg_pitch_count = get_count(transpose_pitch[11])
		row.append(seg_pitch_count)
	        seg_pitch_sum = get_sum(transpose_pitch[11])
		row.append(seg_pitch_sum)   
		#timbre arrays
	        seg_timbre = hdf5_getters.get_segments_timbre(h5)
                transpose_timbre = seg_pitch.transpose() #tranposing matrix, to have 12 rows
		row.append(transpose_timbre[0][i])
  		seg_timbre_avg= get_avg(transpose_timbre[0])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[0])	
		row.append(seg_timbre_max)
		seg_timbre_min = get_min(transpose_timbre[0])
		row.append(seg_timbre_min)
		seg_timbre_stddev=get_stddev(transpose_timbre[0])
		row.append(seg_timbre_stddev)
		seg_timbre_count = get_count(transpose_timbre[0])
		row.append(seg_timbre_count)
		seg_timbre_sum = get_sum(transpose_timbre[0])
		row.append(seg_timbre_sum)   
 		row.append(transpose_timbre[1][i])
 		seg_timbre_avg= get_avg(transpose_timbre[1])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[1])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[1])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[1])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[1])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[1])
		row.append(seg_timbre_sum)   
		row.append(transpose_timbre[2][i])
 		seg_timbre_avg= get_avg(transpose_timbre[2])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[2])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[2])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[2])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[2])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[2])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[3][i])
 		seg_timbre_avg= get_avg(transpose_timbre[3])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[3])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[3])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[3])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[3])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[3])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[4][i])
 		seg_timbre_avg= get_avg(transpose_timbre[4])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[4])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[4])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[4])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[4])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[4])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[5][i])
 		seg_timbre_avg= get_avg(transpose_timbre[5])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[5])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[5])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[5])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[5])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[5])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[6][i])
 		seg_timbre_avg= get_avg(transpose_timbre[6])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[6])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[6])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[6])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[6])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[6])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[7][i])
 		seg_timbre_avg= get_avg(transpose_timbre[7])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[7])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[7])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[7])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[7])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[7])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[8][i])
 		seg_timbre_avg= get_avg(transpose_timbre[8])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[8])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[8])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[8])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[8])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[8])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[9][i])
 		seg_timbre_avg= get_avg(transpose_timbre[9])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[9])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[9])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[9])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[9])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[9])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[10][i])
 		seg_timbre_avg= get_avg(transpose_timbre[10])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[10])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[10])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[10])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[10])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[10])
		row.append(seg_timbre_sum)   
		
		row.append(transpose_timbre[11][i])
 		seg_timbre_avg= get_avg(transpose_timbre[11])
		row.append(seg_timbre_avg)
		seg_timbre_max= get_max(transpose_timbre[11])	
		row.append(seg_timbre_max)
	        seg_timbre_min = get_min(transpose_timbre[11])
		row.append(seg_timbre_min)
	        seg_timbre_stddev= get_stddev(transpose_timbre[11])
		row.append(seg_timbre_stddev)
	        seg_timbre_count = get_count(transpose_timbre[11])
		row.append(seg_timbre_count)
	        seg_timbre_sum = get_sum(transpose_timbre[11])
		row.append(seg_timbre_sum)
	        for item in row_seg2_padding:
			row.append(item)
		writer.writerow(row)
		row=[]
		row=gral_info[:]


            # "--------tatums---------------"
	    tatms_c = hdf5_getters.get_tatums_confidence(h5)
	    group_index=5
	    row_front=padding(245)	#blank spaces left in front of tatums
	    row=[]
	    row=gral_info[:]
	    for i,item in enumerate(tatms_c):
		row.append(group_index)
		row.append(i)
		for item in row_front:	#appending blank spaces at the front of the row
			row.append(item)

		row.append(tatms_c[i])
		tatms_c_avg= get_avg(tatms_c)
		row.append(tatms_c_avg)
	 	tatms_c_max= get_max(tatms_c)
		row.append(tatms_c_max)
	        tatms_c_min = get_min(tatms_c)
		row.append(tatms_c_min)
	        tatms_c_stddev= get_stddev(tatms_c)
		row.append(tatms_c_stddev)
                tatms_c_count = get_count(tatms_c)
		row.append(tatms_c_count)
                tatms_c_sum = get_sum(tatms_c)
		row.append(tatms_c_sum)
                tatms_start = hdf5_getters.get_tatums_start(h5)
		row.append(tatms_start[i])
	        tatms_start_avg= get_avg(tatms_start)
		row.append(tatms_start_avg)
	        tatms_start_max= get_max(tatms_start)
		row.append(tatms_start_max)
	        tatms_start_min = get_min(tatms_start)
		row.append(tatms_start_min)
	        tatms_start_stddev= get_stddev(tatms_start)
		row.append(tatms_start_stddev)
	        tatms_start_count = get_count(tatms_start)
		row.append(tatms_start_count)
	        tatms_start_sum = get_sum(tatms_start)				   
		row.append(tatms_start_sum)
		writer.writerow(row)
		row=[]
		row=gral_info[:]


 
	    transpose_pitch= seg_pitch.transpose() #this is to tranpose the matrix,so we can have 12 rows
	    #arrays containing the aggregate values of the 12 rows
	    seg_pitch_avg=[]
	    seg_pitch_max=[]
	    seg_pitch_min=[]
            seg_pitch_stddev=[]
            seg_pitch_count=[]
	    seg_pitch_sum=[]
            i=0
	    #Getting the aggregate values in the pitches array
	    for row in transpose_pitch:
		   seg_pitch_avg.append(get_avg(row))
		   seg_pitch_max.append(get_max(row))
	           seg_pitch_min.append(get_min(row))
		   seg_pitch_stddev.append(get_stddev(row))
		   seg_pitch_count.append(get_count(row))
                   seg_pitch_sum.append(get_sum(row))
		   i=i+1

	    #extracting information from the timbre array 
            transpose_timbre = seg_pitch.transpose() #tranposing matrix, to have 12 rows
	    #arrays containing the aggregate values of the 12 rows
	    seg_timbre_avg=[]
	    seg_timbre_max=[]
	    seg_timbre_min=[]
            seg_timbre_stddev=[]
            seg_timbre_count=[]
	    seg_timbre_sum=[]
            i=0
	    for row in transpose_timbre:
		   seg_timbre_avg.append(get_avg(row))
		   seg_timbre_max.append(get_max(row))
	           seg_timbre_min.append(get_min(row))
		   seg_timbre_stddev.append(get_stddev(row))
		   seg_timbre_count.append(get_count(row))
                   seg_timbre_sum.append(get_sum(row))
		   i=i+1








	    h5.close()
	    count=count+1;
	    print count;
		
#change the directory to the one you want
data_to_flat_file("HDF5");
