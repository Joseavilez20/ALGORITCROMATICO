import os
#Librerias reportlab a usar:
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch

##A = [2726, 2697, 2765, 2976, 3025, 2884, 2724, 2634, 2828, 2682, 2725, 2670, 2696, 2735, 2817, 3008, 2880, 3008, 2878, 2908, 2934, 3004, 2975, 3020, 3276, 2887, 3320, 3350, 3920, 3908, 3725, 3586, 3574, 3531, 3462, 3512, 3527, 3647, 3681, 3723, 3762, 3749, 3525, 3628, 3642, 3713, 3734, 3620, 3730, 3879, 3902, 3810, 3962, 3859, 3731, 3619, 3814, 3615, 3592, 3780, 3392, 3613, 3856, 4110, 3889, 3903, 3660, 3648, 3658, 3606, 3568, 3637]
##B = [2551.3, 2566.1, 2615.2, 2704.8, 2829.4, 2706.2, 2802.4, 2781.5, 2755.6, 2714.2, 2775.8, 2693.0, 2675.9, 2694.1, 2675.4, 2706.2, 2864.5, 2860.3, 2974.1, 2963.4, 3014.5, 3094.0, 3145.8, 3189.4, 3275.7, 3297.5, 3363.2, 3443.1, 3407.9, 3542.8, 3480.3, 3527.9, 3512.8, 3520.3, 3614.9, 3597.9, 3575.7, 3590.3, 3631.3, 3728.1, 3634.1, 3711.3, 3784.3, 3788.4, 3714.4, 3688.6, 3704.4, 3804.9, 3720.0, 3698.8, 3738.6, 3772.5, 3768.7, 3773.1, 3738.2, 3745.2, 3753.3, 3794.5, 3798.1, 3726.8, 3818.9, 3890.4, 3868.5, 3870.5, 3786.9, 3819.8, 3801.6, 3770.4, 3797.2, 3748.8, 3775.5, 3764.4, 3747.8, 3747.4, 3767.7, 3755.1, 3761.9, 3757.0, 3755.6, 3754.4, 3751.7, 3764.9, 3760.2, 3753.8]

def generarPDF(A,B):
##    general = []
##    for k in largs:
##        general.append(k)
    doc = SimpleDocTemplate("test.pdf", pagesize = A4)
    story=[]
    lista = []
    for i in zip(A,B):
        lista.append(i)
    datos = tuple(lista)


    tabla = Table(data = datos,colWidths=[1*inch,3*inch,3*inch,3*inch, 3*inch],
                  style = [
                           ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                           ('BOX',(0,0),(-1,-1),2,colors.black),
                           ('BACKGROUND', (0, 0), (-1, 0), colors.lavender),
                           ]
                  )

    story.append(tabla)
    story.append(Spacer(0,15))
    doc.build(story)
    os.system("test.pdf")






