import sys
import math

def main():
    for line in sys.stdin:
        line = line.rstrip('\n')
        
        hr = line[0:4]
        s = hr + ','

        name = line[4:14]
        s = s + name + ','

        dm = line[14:25]
        s = s + dm + ','

        hd = line[25:31]
        s = s + hd + ','

        sao = line[31:37]
        s = s + sao + ','

        fk5 = line[37:41]
        s = s + fk5 + ','

        irflag = line[41:42]
        s = s + irflag + ','

        r_irflag = line[42:43]
        s = s + r_irflag + ','

        multiple = line [43:44]
        s = s + multiple + ','

        #NEED TO CHANGE INTO FLOAT DT (degrees)
        #GOES FROM -PI TO PI
        glon = line[90:96]
        s = s + glon + ','


        #GOES FROM -PI/2 TO PI/2
        glat = line[96:102]
        s = s + glat + ','

        #NEED TO COLOR CODE USING ANOTHER COLUMN? IF NO TYPE THEN ASSIGN BLACK
        sptype = line[127:147]
        s = s + sptype + ','

        #ra_deg = 15 * (rah + ram/60 + ras/3600)

        #INT
        rah = line[75:77]
        s = s + rah + ','

        #INT
        ram = line[75:77]
        s = s + ram + ','

        #FLOAT
        ras = line[75:77]
        s = s + ras + ','

        #DEC_deg = (ded + dem/60 + des/3600)

        de_minus = line[83:84]
        s = s + de_minus + ','

        #INT
        ded = line[84:86]
        s = s + ded + ','
        
        #INT
        dem = line[86:88]
        s = s + dem + ','

        #INT
        des = line[88:90]
        s = s + des + ','

        print (s)







    



if __name__ == "__main__":
  main()