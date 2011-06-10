/*
###########################################################
###                   Infobright 2011                   ###
###            Developed by: Infobright Intern Team     ###
###                 Author: Infobright Intern Team      ###
###                     Version 1.0                     ###
###                                                     ###
### v1.0 Infobright Intern Team                         ###
### 									                ###
###                                                     ###
### The MIT License                                     ###
###                                                     ###
### Copyright (c) 2010 Infobright Inc.                  ###
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
# Usage                                                  #h
#                                                        #h
# mysql-ib -u root < Million_Song_DDL.sql                #h
#                                                        #h
##########################################################h*/


DROP DATABASE IF EXISTS Music;

CREATE DATABASE IF NOT EXISTS Music;

USE Music;

CREATE TABLE Metadata(
title VARCHAR(400), album VARCHAR(400), artist VARCHAR(400),duration FLOAT, sample_rate FLOAT,artist_7digitalid INT, artist_familiarity FLOAT,
artist_hotness FLOAT, artiset_id VARCHAR(100),artist_latitude FLOAT, artist_location VARCHAR(100),artist_longitude FLOAT,
artist_mbid VARCHAR(100),hip_hop BOOLEAN,pop_rock BOOLEAN,new_wave BOOLEAN,
jazz BOOLEAN,reggae BOOLEAN,disco BOOLEAN,comedy BOOLEAN,soul BOOLEAN,ballad BOOLEAN,ragtime BOOLEAN, male_vocalist BOOLEAN,tango BOOLEAN, dubstep BOOLEAN,soundtrack BOOLEAN,cumbia BOOLEAN,big_band BOOLEAN,
bluegrass BOOLEAN,opera BOOLEAN,tejano BOOLEAN,trip_hop BOOLEAN, blues BOOLEAN,trance BOOLEAN,mambo BOOLEAN,salsa BOOLEAN,pop BOOLEAN,rapcore BOOLEAN,orchestra BOOLEAN,swing BOOLEAN,freestyle BOOLEAN,techno BOOLEAN, 
dance BOOLEAN, mariachi BOOLEAN,celtic BOOLEAN,oldies BOOLEAN,punk BOOLEAN,merengue BOOLEAN, karaokee BOOLEAN, latin BOOLEAN, 8bit BOOLEAN, gospel BOOLEAN, bossa_nova BOOLEAN, electronic BOOLEAN, polka BOOLEAN,
new_age BOOLEAN, dj BOOLEAN,country BOOLEAN,ranchera BOOLEAN,chinese BOOLEAN, ska BOOLEAN,christian BOOLEAN, rock BOOLEAN, classical BOOLEAN, concerto BOOLEAN,experimental BOOLEAN,rap BOOLEAN, folk BOOLEAN, waltz BOOLEAN,
 guitar BOOLEAN,female_vocalist BOOLEAN,portuguese BOOLEAN, hardcore BOOLEAN,latin_pop BOOLEAN,metal BOOLEAN,italian BOOLEAN,remix BOOLEAN,progressive BOOLEAN, alternative BOOLEAN, japanese BOOLEAN,
  ambient BOOLEAN, choral_music BOOLEAN,instrumental BOOLEAN,swedish BOOLEAN, tropical BOOLEAN,urban BOOLEAN, dutch BOOLEAN,piano BOOLEAN,american BOOLEAN, spanish BOOLEAN, romantic BOOLEAN,
  cowboy BOOLEAN,christmas_music BOOLEAN, spiritual BOOLEAN,brazilian BOOLEAN,singer_songwriter BOOLEAN,indie BOOLEAN, 
break_beat BOOLEAN, religious BOOLEAN, rare_grove BOOLEAN, world BOOLEAN,rhythm_and_blues BOOLEAN,easy_listening BOOLEAN,industrial BOOLEAN,house BOOLEAN, 
avant_garde BOOLEAN,spoken_word BOOLEAN,fusion BOOLEAN, glam BOOLEAN,british_invasion BOOLEAN, funk BOOLEAN, parlophone BOOLEAN, britpop BOOLEAN,grunge BOOLEAN,greek BOOLEAN,chanson BOOLEAN,swiss BOOLEAN,ghetto_tech BOOLEAN,
thrash_core BOOLEAN,patriotic BOOLEAN,humppa BOOLEAN,turnablism BOOLEAN,mexican BOOLEAN,canadian BOOLEAN,french BOOLEAN,meditation BOOLEAN,soukous BOOLEAN,ost BOOLEAN,flamenco BOOLEAN,screamo BOOLEAN,
freakbeat BOOLEAN,melbourne BOOLEAN,africa BOOLEAN,eurodance BOOLEAN,accordion BOOLEAN,german BOOLEAN,ethnic BOOLEAN,bhangra BOOLEAN,gaita BOOLEAN, san_francisco_bay_area BOOLEAN,
cajun BOOLEAN,jungle_music BOOLEAN,marimba BOOLEAN,musette BOOLEAN,united_states BOOLEAN,artist_playmeid INT, audio_md5 VARCHAR(100),
danceability FLOAT, end_fade_in FLOAT,energy FLOAT,song_key INT,key_confidence FLOAT, loudness FLOAT, mode INT, mode_confidence FLOAT, release_7digitalid INT, song_hotness FLOAT,
song_id VARCHAR(100),start_fade_out FLOAT, tempo FLOAT, time_signature INT, time_signature_confidence FLOAT,track_id VARCHAR(100),track_7digitalid INT, year INT, bars_confidence_avg FLOAT, bars_confidence_max FLOAT,
bars_confidence_min FLOAT,bars_confidence_stddev FLOAT, bars_confidence_count FLOAT,bars_confidence_sum FLOAT,bars_start_avg FLOAT,bars_start_max FLOAT, bars_start_min FLOAT, bars_start_stddev FLOAT,
bars_start_count INT,bars_start_sum FLOAT, beats_confidence_avg FLOAT, beats_confidence_max FLOAT,beats_confidence_min FLOAT, beats_confidence_stddev FLOAT,
  beats_confidence_count INT,beats_confidence_sum FLOAT,beats_start_avg FLOAT,beats_start_max FLOAT,beats_start_min FLOAT, beats_start_stddev FLOAT,beats_start_count INT, beats_start_sum FLOAT,sections_confidence_avg FLOAT,sections_confidence_max FLOAT, 
  sections_confidence_min FLOAT, sections_confidence_stddev FLOAT,sections_confidence_count INT,sections_confidence_sum FLOAT,sections_start_avg FLOAT,sections_start_max FLOAT,sections_start_min FLOAT,
  sections_start_stddev FLOAT,sections_start_count INT,sections_start_sum FLOAT,segments_confidence_avg FLOAT,segments_confidence_max FLOAT, segments_confidence_min FLOAT,segments_confidence_stddev FLOAT,segments_confidence_count INT,
  segments_confidence_sum FLOAT,segments_loudness_max_avg FLOAT,segments_loudness_max_max FLOAT,segments_loudness_max_min FLOAT,segments_lodness_max_stddev FLOAT,segments_lodness_max_count INT,segments_loudness_max_sum FLOAT, 
  segments_loudness_max_time_avg FLOAT, segments_loudness_max_time_max FLOAT,segments_loudness_max_time_min FLOAT,segments_loudness_max_time_stddev FLOAT,segments_loudness_max_time_count FLOAT,
  segments_loudness_max_time_sum FLOAT,segments_loudness_start_avg FLOAT,segments_loudness_start_max FLOAT,segments_loudness_start_min FLOAT,segments_loudness_start_stddev FLOAT,
  segments_loudness_start_count INT,segments_loudness_start_sum FLOAT,segments_pitches_0_avg FLOAT,segments_pitches_0_max FLOAT,segments_pitches_0_min FLOAT,segments_pitches_0_stddev FLOAT,
  segments_pitches_0_count INT,segments_pitches_0_sum FLOAT, segments_pitches_1_avg FLOAT,segments_pitches_1_max FLOAT,segments_pitches_1_min FLOAT,segments_pitches_1_stddev FLOAT,segments_pitches_1_count INT,
  segments_pitches_1_sum FLOAT,segments_pitches_2_avg FLOAT,segments_pitches_2_max FLOAT,segments_pitches_2_min FLOAT,segments_pitches_2_stddev FLOAT,segments_pitches_2_count INT,segments_pitches_2_sum FLOAT,
  segments_pitches_3_avg FLOAT,segments_pitches_3_max FLOAT,segments_pitches_3_min FLOAT,segments_pitches_3_stddev FLOAT,segments_pitches_3_count INT,segments_pitches_3_sum FLOAT, segments_pitches_4_avg FLOAT,
  segments_pitches_4_max FLOAT,segments_pitches_4_min FLOAT,segments_pitches_4_stddev FLOAT,segments_pitches_4_count INT,segments_pitches_4_sum FLOAT, segments_pitches_5_avg FLOAT,segments_pitches_5_max FLOAT,
  segments_pitches_5_min FLOAT,segments_pitches_5_stddev FLOAT,segments_pitches_5_count INT,segments_pitches_5_sum FLOAT, segments_pitches_6_avg FLOAT,segments_pitches_6_max FLOAT,segments_pitches_6_min FLOAT,
  segments_pitches_6_stddev FLOAT,segments_pitches_6_count INT,segments_pitches_6_sum FLOAT, segments_pitches_7_avg FLOAT,segments_pitches_7_max FLOAT,segments_pitches_7_min FLOAT,segments_pitches_7_stddev FLOAT,
  segments_pitches_7_count INT,segments_pitches_7_sum FLOAT,segments_pitches_8_avg FLOAT,segments_pitches_8_max FLOAT,segments_pitches_8_min FLOAT,segments_pitches_8_stddev FLOAT,segments_pitches_8_count INT,
  segments_pitches_8_sum FLOAT, segments_pitches_9_avg FLOAT,segments_pitches_9_max FLOAT,segments_pitches_9_min FLOAT,segments_pitches_9_stddev FLOAT,segments_pitches_9_count INT,segments_pitches_9_sum FLOAT, 
  segments_pitches_10_avg FLOAT,segments_pitches_10_max FLOAT,segments_pitches_10_min FLOAT,segments_pitches_10_stddev FLOAT,segments_pitches_10_count INT,segments_pitches_10_sum FLOAT, segments_pitches_11_avg FLOAT,
  segments_pitches_11_max FLOAT,segments_pitches_11_min FLOAT,segments_pitches_11_stddev FLOAT,segments_pitches_11_count INT,segments_pitches_11_sum FLOAT,segments_start_avg FLOAT,segments_start_max FLOAT,
  segments_start_min FLOAT, segments_start_stddev FLOAT,segments_start_count FLOAT, segments_start_sum FLOAT,segments_timbre_0_avg FLOAT,segments_timbre_0_max FLOAT,segments_timbre_0_min FLOAT,
  segments_timbre_0_stddev FLOAT,segments_timbre_0_count INT,segments_timbre_0_sum FLOAT,segments_timbre_1_avg FLOAT,segments_timbre_1_max FLOAT,segments_timbre_1_min FLOAT,
  segments_timbre_1_stddev FLOAT,segments_timbre_1_count INT,segments_timbre_1_sum FLOAT,segments_timbre_2_avg FLOAT,segments_timbre_2_max FLOAT,segments_timbre_2_min FLOAT,
  segments_timbre_2_stddev FLOAT,segments_timbre_2_count INT,segments_timbre_2_sum FLOAT,segments_timbre_3_avg FLOAT,segments_timbre_3_max FLOAT,segments_timbre_3_min FLOAT,
  segments_timbre_3_stddev FLOAT,segments_timbre_3_count INT,segments_timbre_3_sum FLOAT,segments_timbre_4_avg FLOAT,segments_timbre_4_max FLOAT,segments_timbre_4_min FLOAT,
  segments_timbre_4_stddev FLOAT,segments_timbre_4_count INT,segments_timbre_4_sum FLOAT,segments_timbre_5_avg FLOAT,segments_timbre_5_max FLOAT,segments_timbre_5_min FLOAT,
  segments_timbre_5_stddev FLOAT,segments_timbre_5_count INT,segments_timbre_5_sum FLOAT,segments_timbre_6_avg FLOAT,segments_timbre_6_max FLOAT,segments_timbre_6_min FLOAT,
  segments_timbre_6_stddev FLOAT,segments_timbre_6_count INT,segments_timbre_6_sum FLOAT,segments_timbre_7_avg FLOAT,segments_timbre_7_max FLOAT,segments_timbre_7_min FLOAT,
  segments_timbre_7_stddev FLOAT,segments_timbre_7_count INT,segments_timbre_7_sum FLOAT,segments_timbre_8_avg FLOAT,segments_timbre_8_max FLOAT,segments_timbre_8_min FLOAT,
  segments_timbre_8_stddev FLOAT,segments_timbre_8_count INT,segments_timbre_8_sum FLOAT,segments_timbre_9_avg FLOAT,segments_timbre_9_max FLOAT,segments_timbre_9_min FLOAT,
  segments_timbre_9_stddev FLOAT,segments_timbre_9_count INT,segments_timbre_9_sum FLOAT,segments_timbre_10_avg FLOAT,segments_timbre_10_max FLOAT,segments_timbre_10_min FLOAT,
  segments_timbre_10_stddev FLOAT,segments_timbre_10_count INT,segments_timbre_10_sum FLOAT,segments_timbre_11_avg FLOAT,segments_timbre_11_max FLOAT,segments_timbre_11_min FLOAT,
  segments_timbre_11_stddev FLOAT,segments_timbre_11_count INT,segments_timbre_11_sum FLOAT,tatums_confidence_avg FLOAT,tatums_confidence_max FLOAT,tatums_confidence_min FLOAT,tatums_confidence_stddev FLOAT,tatums_confidence_count INT,
  tatums_confidence_sum FLOAT, tatums_start_avg FLOAT, tatums_start_max FLOAT,tatums_start_min FLOAT,tatums_start_stddev FLOAT,tatums_start_count INT,tatums_start_sum FLOAT) CHARACTER SET utf8 COLLATE utf8_bin;

CREATE TABLE CompleteTable(
title VARCHAR(400), album VARCHAR(400), artist VARCHAR(400),duration FLOAT, sample_rate FLOAT,artist_7digitalid INT, artist_familiarity FLOAT,
artist_hotness FLOAT, artiset_id VARCHAR(100),artist_latitude FLOAT, artist_location VARCHAR(100),artist_longitude FLOAT,
artist_mbid VARCHAR(100),hip_hop BOOLEAN,pop_rock BOOLEAN,new_wave BOOLEAN,
jazz BOOLEAN,reggae BOOLEAN,disco BOOLEAN,comedy BOOLEAN,soul BOOLEAN,ballad BOOLEAN,ragtime BOOLEAN, male_vocalist BOOLEAN,tango BOOLEAN, dubstep BOOLEAN,soundtrack BOOLEAN,cumbia BOOLEAN,big_band BOOLEAN,
bluegrass BOOLEAN,opera BOOLEAN,tejano BOOLEAN,trip_hop BOOLEAN, blues BOOLEAN,trance BOOLEAN,mambo BOOLEAN,salsa BOOLEAN,pop BOOLEAN,rapcore BOOLEAN,orchestra BOOLEAN,swing BOOLEAN,freestyle BOOLEAN,techno BOOLEAN, 
dance BOOLEAN, mariachi BOOLEAN,celtic BOOLEAN,oldies BOOLEAN,punk BOOLEAN,merengue BOOLEAN, karaokee BOOLEAN, latin BOOLEAN, 8bit BOOLEAN, gospel BOOLEAN, bossa_nova BOOLEAN, electronic BOOLEAN, polka BOOLEAN,
new_age BOOLEAN, dj BOOLEAN,country BOOLEAN,ranchera BOOLEAN,chinese BOOLEAN, ska BOOLEAN,christian BOOLEAN, rock BOOLEAN, classical BOOLEAN, concerto BOOLEAN,experimental BOOLEAN,rap BOOLEAN, folk BOOLEAN, waltz BOOLEAN,
 guitar BOOLEAN,female_vocalist BOOLEAN,portuguese BOOLEAN, hardcore BOOLEAN,latin_pop BOOLEAN,metal BOOLEAN,italian BOOLEAN,remix BOOLEAN,progressive BOOLEAN, alternative BOOLEAN, japanese BOOLEAN,
  ambient BOOLEAN, choral_music BOOLEAN,instrumental BOOLEAN,swedish BOOLEAN, tropical BOOLEAN,urban BOOLEAN, dutch BOOLEAN,piano BOOLEAN,american BOOLEAN, spanish BOOLEAN, romantic BOOLEAN,
  cowboy BOOLEAN,christmas_music BOOLEAN, spiritual BOOLEAN,brazilian BOOLEAN,singer_songwriter BOOLEAN,indie BOOLEAN, 
break_beat BOOLEAN, religious BOOLEAN, rare_grove BOOLEAN, world BOOLEAN,rhythm_and_blues BOOLEAN,easy_listening BOOLEAN,industrial BOOLEAN,house BOOLEAN, 
avant_garde BOOLEAN,spoken_word BOOLEAN,fusion BOOLEAN, glam BOOLEAN,british_invasion BOOLEAN, funk BOOLEAN, parlophone BOOLEAN, britpop BOOLEAN,grunge BOOLEAN,greek BOOLEAN,chanson BOOLEAN,swiss BOOLEAN,ghetto_tech BOOLEAN,
thrash_core BOOLEAN,patriotic BOOLEAN,humppa BOOLEAN,turnablism BOOLEAN,mexican BOOLEAN,canadian BOOLEAN,french BOOLEAN,meditation BOOLEAN,soukous BOOLEAN,ost BOOLEAN,flamenco BOOLEAN,screamo BOOLEAN,
freakbeat BOOLEAN,melbourne BOOLEAN,africa BOOLEAN,eurodance BOOLEAN,accordion BOOLEAN,german BOOLEAN,ethnic BOOLEAN,bhangra BOOLEAN,gaita BOOLEAN, san_francisco_bay_area BOOLEAN,
cajun BOOLEAN,jungle_music BOOLEAN,marimba BOOLEAN,musette BOOLEAN,united_states BOOLEAN,artist_playmeid INT, audio_md5 VARCHAR(100),
danceability FLOAT, end_fade_in FLOAT,energy FLOAT,song_key INT,key_confidence FLOAT, loudness FLOAT, mode INT, mode_confidence FLOAT, release_7digitalid INT, song_hotness FLOAT,
song_id VARCHAR(100),start_fade_out FLOAT, tempo FLOAT, time_signature INT, time_signature_confidence FLOAT,track_id VARCHAR(100),track_7digitalid INT, year INT, group_index INT,array_index INT,bars_confidence FLOAT,bars_confidence_avg FLOAT, bars_confidence_max FLOAT,
bars_confidence_min FLOAT,bars_confidence_stddev FLOAT, bars_confidence_count FLOAT,bars_confidence_sum FLOAT,bars_start FLOAT,bars_start_avg FLOAT,bars_start_max FLOAT, bars_start_min FLOAT, bars_start_stddev FLOAT,
bars_start_count INT,bars_start_sum FLOAT, beats_confidence FLOAT, beats_confidence_avg FLOAT, beats_confidence_max FLOAT,beats_confidence_min FLOAT, beats_confidence_stddev FLOAT,
  beats_confidence_count INT,beats_confidence_sum FLOAT,beats_start FLOAT,beats_start_avg FLOAT,beats_start_max FLOAT,beats_start_min FLOAT, beats_start_stddev FLOAT,beats_start_count INT, beats_start_sum FLOAT,
  sections_confidence FLOAT,sections_confidence_avg FLOAT,sections_confidence_max FLOAT, 
  sections_confidence_min FLOAT, sections_confidence_stddev FLOAT,sections_confidence_count INT,sections_confidence_sum FLOAT,sections_start FLOAT,sections_start_avg FLOAT,sections_start_max FLOAT,sections_start_min FLOAT,
  sections_start_stddev FLOAT,sections_start_count INT,sections_start_sum FLOAT,segments_confidence FLOAT,segments_confidence_avg FLOAT,segments_confidence_max FLOAT, segments_confidence_min FLOAT,segments_confidence_stddev FLOAT,segments_confidence_count INT,
  segments_confidence_sum FLOAT,segments_loudness_max FLOAT,segments_loudness_max_avg FLOAT,segments_loudness_max_max FLOAT,segments_loudness_max_min FLOAT,segments_lodness_max_stddev FLOAT,segments_lodness_max_count INT,
  segments_loudness_max_sum FLOAT, segments_loudness_max_time FLOAT,segments_loudness_max_time_avg FLOAT, segments_loudness_max_time_max FLOAT,
  segments_loudness_max_time_min FLOAT,segments_loudness_max_time_stddev FLOAT,segments_loudness_max_time_count FLOAT,
  segments_loudness_max_time_sum FLOAT,segments_loudness_start FLOAT,segments_loudness_start_avg FLOAT,segments_loudness_start_max FLOAT,segments_loudness_start_min FLOAT,segments_loudness_start_stddev FLOAT,
  segments_loudness_start_count INT,segments_loudness_start_sum FLOAT,
  segments_start FLOAT,segments_start_avg FLOAT,segments_start_max FLOAT,segments_start_min FLOAT, segments_start_stddev FLOAT,segments_start_count FLOAT, segments_start_sum FLOAT,
  segments_pitches_0 FLOAT,segments_pitches_0_avg FLOAT,segments_pitches_0_max FLOAT,segments_pitches_0_min FLOAT,segments_pitches_0_stddev FLOAT,
  segments_pitches_0_count INT,segments_pitches_0_sum FLOAT, segments_pitches_1 FLOAT,segments_pitches_1_avg FLOAT,segments_pitches_1_max FLOAT,segments_pitches_1_min FLOAT,segments_pitches_1_stddev FLOAT,segments_pitches_1_count INT,
  segments_pitches_1_sum FLOAT,segments_pitches_2 FLOAT,segments_pitches_2_avg FLOAT,segments_pitches_2_max FLOAT,segments_pitches_2_min FLOAT,segments_pitches_2_stddev FLOAT,segments_pitches_2_count INT,
  segments_pitches_2_sum FLOAT,segments_pitches_3 FLOAT, segments_pitches_3_avg FLOAT,segments_pitches_3_max FLOAT,segments_pitches_3_min FLOAT,segments_pitches_3_stddev FLOAT,segments_pitches_3_count INT,
  segments_pitches_3_sum FLOAT, segments_pitches_4 FLOAT,segments_pitches_4_avg FLOAT,segments_pitches_4_max FLOAT,segments_pitches_4_min FLOAT,segments_pitches_4_stddev FLOAT,
  segments_pitches_4_count INT,segments_pitches_4_sum FLOAT, segments_pitches_5 FLOAT,segments_pitches_5_avg FLOAT,segments_pitches_5_max FLOAT,segments_pitches_5_min FLOAT,segments_pitches_5_stddev FLOAT,segments_pitches_5_count INT,
  segments_pitches_5_sum FLOAT, segments_pitches_6 FLOAT, segments_pitches_6_avg FLOAT,segments_pitches_6_max FLOAT,segments_pitches_6_min FLOAT,
  segments_pitches_6_stddev FLOAT,segments_pitches_6_count INT,segments_pitches_6_sum FLOAT, segments_pitches_7 FLOAT,segments_pitches_7_avg FLOAT,segments_pitches_7_max FLOAT,segments_pitches_7_min FLOAT,segments_pitches_7_stddev FLOAT,
  segments_pitches_7_count INT,segments_pitches_7_sum FLOAT,segments_pitches_8 FLOAT,segments_pitches_8_avg FLOAT,segments_pitches_8_max FLOAT,segments_pitches_8_min FLOAT,segments_pitches_8_stddev FLOAT,segments_pitches_8_count INT,
  segments_pitches_8_sum FLOAT, segments_pitches_9 FLOAT,segments_pitches_9_avg FLOAT,segments_pitches_9_max FLOAT,segments_pitches_9_min FLOAT,segments_pitches_9_stddev FLOAT,segments_pitches_9_count INT,
  segments_pitches_9_sum FLOAT, segments_pitches_10 FLOAT,segments_pitches_10_avg FLOAT,segments_pitches_10_max FLOAT,segments_pitches_10_min FLOAT,segments_pitches_10_stddev FLOAT,
  segments_pitches_10_count INT,segments_pitches_10_sum FLOAT, segments_pitches_11 FLOAT,segments_pitches_11_avg FLOAT,
  segments_pitches_11_max FLOAT,segments_pitches_11_min FLOAT,segments_pitches_11_stddev FLOAT,segments_pitches_11_count INT,segments_pitches_11_sum FLOAT,
  segments_timbre_0 FLOAT,segments_timbre_0_avg FLOAT,segments_timbre_0_max FLOAT,segments_timbre_0_min FLOAT,
  segments_timbre_0_stddev FLOAT,segments_timbre_0_count INT,segments_timbre_0_sum FLOAT,segments_timbre_1 FLOAT,segments_timbre_1_avg FLOAT,segments_timbre_1_max FLOAT,segments_timbre_1_min FLOAT,
  segments_timbre_1_stddev FLOAT,segments_timbre_1_count INT,segments_timbre_1_sum FLOAT,segments_timbre_2 FLOAT,segments_timbre_2_avg FLOAT,segments_timbre_2_max FLOAT,segments_timbre_2_min FLOAT,
  segments_timbre_2_stddev FLOAT,segments_timbre_2_count INT,segments_timbre_2_sum FLOAT,segments_timbre_3 FLOAT,segments_timbre_3_avg FLOAT,segments_timbre_3_max FLOAT,segments_timbre_3_min FLOAT,
  segments_timbre_3_stddev FLOAT,segments_timbre_3_count INT,segments_timbre_3_sum FLOAT,segments_timbre_4 FLOAT,segments_timbre_4_avg FLOAT,segments_timbre_4_max FLOAT,segments_timbre_4_min FLOAT,
  segments_timbre_4_stddev FLOAT,segments_timbre_4_count INT,segments_timbre_4_sum FLOAT,segments_timbre_5 FLOAT,segments_timbre_5_avg FLOAT,segments_timbre_5_max FLOAT,segments_timbre_5_min FLOAT,
  segments_timbre_5_stddev FLOAT,segments_timbre_5_count INT,segments_timbre_5_sum FLOAT,segments_timbre_6 FLOAT,segments_timbre_6_avg FLOAT,segments_timbre_6_max FLOAT,segments_timbre_6_min FLOAT,
  segments_timbre_6_stddev FLOAT,segments_timbre_6_count INT,segments_timbre_6_sum FLOAT,segments_timbre_7 FLOAT,segments_timbre_7_avg FLOAT,segments_timbre_7_max FLOAT,segments_timbre_7_min FLOAT,
  segments_timbre_7_stddev FLOAT,segments_timbre_7_count INT,segments_timbre_7_sum FLOAT,segments_timbre_8 FLOAT,segments_timbre_8_avg FLOAT,segments_timbre_8_max FLOAT,segments_timbre_8_min FLOAT,
  segments_timbre_8_stddev FLOAT,segments_timbre_8_count INT,segments_timbre_8_sum FLOAT,segments_timbre_9 FLOAT,segments_timbre_9_avg FLOAT,segments_timbre_9_max FLOAT,segments_timbre_9_min FLOAT,
  segments_timbre_9_stddev FLOAT,segments_timbre_9_count INT,segments_timbre_9_sum FLOAT,segments_timbre_10 FLOAT,segments_timbre_10_avg FLOAT,segments_timbre_10_max FLOAT,segments_timbre_10_min FLOAT,
  segments_timbre_10_stddev FLOAT,segments_timbre_10_count INT,segments_timbre_10_sum FLOAT,segments_timbre_11 FLOAT,segments_timbre_11_avg FLOAT,segments_timbre_11_max FLOAT,segments_timbre_11_min FLOAT,
  segments_timbre_11_stddev FLOAT,segments_timbre_11_count INT,segments_timbre_11_sum FLOAT,tatums_confidence FLOAT,tatums_confidence_avg FLOAT,tatums_confidence_max FLOAT,tatums_confidence_min FLOAT,tatums_confidence_stddev FLOAT,tatums_confidence_count INT,
  tatums_confidence_sum FLOAT, tatums_start FLOAT,tatums_start_avg FLOAT, tatums_start_max FLOAT,tatums_start_min FLOAT,tatums_start_stddev FLOAT,tatums_start_count INT,tatums_start_sum FLOAT);