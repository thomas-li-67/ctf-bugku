#!/usr/bin/python
# coding=utf-8

'''
wave 格式

00H	4	char	"RIFF"标志
04H	4	long int	文件长度
08H	4	char	"WAVE"标志
0CH	4	char	"fmt"标志
10H	4	　	过渡字节（不定）
14H	2	int	格式类别（10H为PCM形式的声音数据)
16H	2	int	通道数，单声道为1，双声道为2
18H	2	int	采样率（每秒样本数），表示每个通道的播放速度，
1CH	4	long int	波形音频数据传送速率，其值为通道数×每秒数据位数
                           ×每样本的数据位数／8。
                            播放软件利用此值可以估计缓冲区的大小。
20H	2	int	数据块的调整数（按字节算的），其值为通道数×
                            每样本的数据位值／8。播放软件需要一次处理多个该值
                            大小的字节数据，以便将其值用于缓冲区的调整。
22H	2	　	每样本的数据位数，表示每个声道中各个样本的数据位数。
                            如果有多个声道，对每个声道而言，样本大小都一样。
24H	4	char	数据标记符＂data＂
28H	4	long int	语音数据的长度

'''