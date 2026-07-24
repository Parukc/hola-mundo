from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from pathlib import Path

OUT = 'Guia_sindromes_hereditarios_cancer.pdf'

regular='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if Path(regular).exists():
    pdfmetrics.registerFont(TTFont('DV',regular)); pdfmetrics.registerFont(TTFont('DVB',bold))
    F='DV'; FB='DVB'
else:
    F='Helvetica'; FB='Helvetica-Bold'

NAVY=HexColor('#17365D'); BLUE=HexColor('#2F75B5'); PALE=HexColor('#EEF4FA'); GOLD=HexColor('#D9A300'); LG=HexColor('#FFF4CC'); GREEN=HexColor('#548235'); LGR=HexColor('#E2F0D9'); RED=HexColor('#C00000'); LR=HexColor('#FCE4D6'); GRAY=HexColor('#666666'); LGRAY=HexColor('#F2F2F2'); DARK=HexColor('#222222')

ss=getSampleStyleSheet()
ss.add(ParagraphStyle(name='T',parent=ss['Title'],fontName=FB,fontSize=22,leading=27,textColor=NAVY,alignment=1,spaceAfter=14))
ss.add(ParagraphStyle(name='Sub',parent=ss['Normal'],fontName=F,fontSize=11,leading=16,textColor=GRAY,alignment=1,spaceAfter=8))
ss.add(ParagraphStyle(name='H1x',parent=ss['Heading1'],fontName=FB,fontSize=16,leading=20,textColor=NAVY,spaceBefore=8,spaceAfter=7))
ss.add(ParagraphStyle(name='H2x',parent=ss['Heading2'],fontName=FB,fontSize=12.5,leading=16,textColor=BLUE,spaceBefore=7,spaceAfter=4))
ss.add(ParagraphStyle(name='B',parent=ss['BodyText'],fontName=F,fontSize=9.1,leading=13,textColor=DARK,spaceAfter=5))
ss.add(ParagraphStyle(name='S',parent=ss['BodyText'],fontName=F,fontSize=7.4,leading=9.8,textColor=DARK))
ss.add(ParagraphStyle(name='Bul',parent=ss['BodyText'],fontName=F,fontSize=8.9,leading=12.2,leftIndent=12,firstLineIndent=-7,spaceAfter=2))
ss.add(ParagraphStyle(name='BoxT',parent=ss['BodyText'],fontName=FB,fontSize=10,leading=13,textColor=NAVY,spaceAfter=3))

P=lambda t,s='B': Paragraph(t,ss[s])
def bul(t): return P('• '+t,'Bul')
def box(title,body,bg=PALE,border=BLUE):
    t=Table([[P(title,'BoxT')],[P(body)]],colWidths=[17.6*cm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),bg),('BOX',(0,0),(-1,-1),.8,border),('LINEBELOW',(0,0),(-1,0),.5,border),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])); return t

def tab(rows,widths,fs=7.1):
    data=[]
    for r,row in enumerate(rows):
        rr=[]
        for c in row:
            st=ParagraphStyle(name=f'x{r}{len(rr)}',parent=ss['S'],fontName=FB if r==0 else F,fontSize=fs,leading=fs+2,textColor=colors.white if r==0 else DARK)
            rr.append(Paragraph(str(c),st))
        data.append(rr)
    t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    cmds=[('GRID',(0,0),(-1,-1),.35,HexColor('#B7C9DB')),('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),NAVY),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]
    for r in range(1,len(data)):
        if r%2==0: cmds.append(('BACKGROUND',(0,r),(-1,r),PALE))
    t.setStyle(TableStyle(cmds)); return t

def footer(canvas,doc):
    canvas.saveState(); canvas.setFont(F,7); canvas.setFillColor(GRAY)
    if doc.page>1:
        canvas.drawString(1.6*cm,A4[1]-1.0*cm,'Síndromes hereditarios de predisposición al cáncer')
        canvas.line(1.6*cm,A4[1]-1.1*cm,A4[0]-1.6*cm,A4[1]-1.1*cm)
    canvas.drawCentredString(A4[0]/2,.7*cm,f'Página {doc.page}'); canvas.restoreState()

doc=SimpleDocTemplate(OUT,pagesize=A4,leftMargin=1.65*cm,rightMargin=1.65*cm,topMargin=1.5*cm,bottomMargin=1.3*cm,title='Guía de síndromes hereditarios de cáncer')
S=[]
S += [Spacer(1,2.2*cm),P('SÍNDROMES HEREDITARIOS<br/>DE PREDISPOSICIÓN AL CÁNCER','T'),P('Guía completa de los cinco casos clínicos','Sub'),HRFlowable(width='75%',thickness=1.2,color=BLUE,spaceBefore=8,spaceAfter=18),P('HBOC · Lynch · Li-Fraumeni · Cowden/PHTS · Poliposis Adenomatosa Familiar','Sub'),Spacer(1,.7*cm),box('Objetivo','Explicar las clasificaciones, diferencias clínicas y moleculares, función de los genes, pruebas recomendadas y asesoramiento genético de los cinco casos.',LG,GOLD),PageBreak()]

S += [P('1. Conceptos básicos','H1x'),P('<b>Cáncer hereditario:</b> predisposición causada por una variante germinal presente desde la concepción. Se hereda el riesgo, no el cáncer.'),P('<b>Variante germinal:</b> está en prácticamente todas las células y puede transmitirse. <b>Variante somática:</b> aparece en un tejido o tumor y normalmente no se hereda.'),box('Herencia común','Los cinco síndromes tienen herencia autosómica dominante: cada hijo tiene 50 % de probabilidad de heredar la variante. La penetrancia es incompleta, por lo que heredarla no garantiza desarrollar cáncer.',LGR,GREEN),P('Señales de alarma','H2x'),bul('Cáncer a edad temprana.'),bul('Varios familiares afectados en la misma rama familiar.'),bul('Tumores raros o múltiples tumores primarios.'),bul('Patrones típicos: mama-ovario, colon-endometrio, sarcoma-mama-cerebro, pápulas-tiroides-mama, o más de 100 pólipos.')]

S += [P('2. Clasificaciones principales','H1x')]
rows=[['Clasificación clínica','Síndrome','Pista principal'],['Mama-ovario hereditario','HBOC','Mama temprana y ovario'],['Colorrectal no polipósico','Lynch','Colon y endometrio sin poliposis masiva'],['Multitumoral','Li-Fraumeni','Sarcomas y cánceres muy precoces'],['Hamartomatoso','Cowden/PHTS','Pápulas, macrocefalia, tiroides'],['Poliposis adenomatosa','FAP','Cientos o miles de adenomas']]
S += [tab(rows,[5.1*cm,4.1*cm,8.4*cm]),Spacer(1,.25*cm),P('Clasificación molecular','H2x')]
rows=[['Mecanismo','Genes','Función'],['Recombinación homóloga','BRCA1, BRCA2','Reparan roturas de doble cadena'],['Mismatch Repair','MLH1, MSH2, MSH6, PMS2','Corrigen errores de apareamiento'],['Control del daño','TP53','Detiene ciclo, repara o induce apoptosis'],['Freno de crecimiento','PTEN','Inhibe PI3K/AKT/mTOR'],['Control de Wnt','APC','Favorece degradación de beta-catenina']]
S += [tab(rows,[5*cm,5*cm,7.6*cm]),box('Diferencia clave','BRCA1/2 y los genes MMR son reparadores, pero corrigen daños distintos: BRCA repara roturas de doble cadena; MMR corrige errores que aparecen al copiar el ADN.',LG,GOLD),PageBreak()]

S += [P('3. Pruebas genéticas: clasificación y diferencias','H1x')]
rows=[['Prueba','Qué estudia','Mejor utilidad'],['Panel por NGS','Secuencia muchos genes','Variantes puntuales y pequeñas inserciones/deleciones; puede estimar CNV'],['Sanger','Una región específica','Confirmar o estudiar una variante familiar conocida'],['MLPA','Número de copias de exones','Grandes deleciones o duplicaciones'],['IHC MMR','Proteínas del tumor','Detecta pérdida de MLH1/MSH2/MSH6/PMS2'],['MSI','Microsatélites tumorales','Demuestra inestabilidad por deficiencia MMR'],['Prueba germinal','Sangre o saliva','Confirma predisposición hereditaria'],['Prueba tumoral','Tejido del cáncer','Detecta alteraciones somáticas y orienta tratamiento']]
S += [tab(rows,[3.7*cm,6.2*cm,7.7*cm],6.9),box('NGS vs MLPA','NGS lee letras del ADN; MLPA cuenta copias. Por eso se complementan. Una NGS muy sensible para cambios pequeños puede no caracterizar con igual seguridad una deleción completa de uno o varios exones.',LG,GOLD),P('Clasificación de variantes','H2x')]
rows=[['Clase','Interpretación'],['Patogénica','Causa enfermedad y puede guiar manejo'],['Probablemente patogénica','Evidencia fuerte de causalidad'],['VUS','Significado incierto; no debe justificar cirugía por sí sola'],['Probablemente benigna','Muy improbable que cause enfermedad'],['Benigna','No causa el síndrome']]
S += [tab(rows,[5*cm,12.6*cm]),PageBreak()]

def case(title,summary,syndrome,just,genes,function,test,risks,adv,diff):
    S.extend([P(title,'H1x'),box('Caso',summary,LGRAY,GRAY),P('1. Identificación','H2x'),P(syndrome),P('2. Justificación clínica y familiar','H2x')])
    for x in just:S.append(bul(x))
    S.extend([P('3. Genes implicados y prueba genética','H2x'),P('<b>Genes:</b> '+genes),P(function),P('<b>Prueba recomendada:</b> '+test),P('4. Riesgos oncológicos asociados','H2x'),P(risks),P('5. Asesoramiento genético','H2x'),P(adv),box('Diferencia principal',diff,LG,GOLD),PageBreak()])

case('4. Caso 1: HBOC','Mujer de 38 años con cáncer de mama HER2 positivo; madre con ovario a los 50 y tía materna con mama a los 45.','<b>Síndrome:</b> cáncer hereditario de mama y ovario. <b>Herencia:</b> autosómica dominante.', ['Mama antes de los 50 años.','Cáncer de ovario en familiar de primer grado.','Dos cánceres de mama/ovario en la misma rama.','HER2 positivo no confirma ni excluye BRCA.'], 'BRCA1 y BRCA2; también PALB2, TP53, CHEK2, ATM según panel.', '<b>BRCA1/2</b> son supresores tumorales que reparan roturas de doble cadena por recombinación homóloga. BRCA2 trabaja estrechamente con RAD51. Su pérdida causa inestabilidad cromosómica.', 'Panel germinal multigénico por NGS con análisis de deleciones/duplicaciones; MLPA si el método no cubre bien CNV.', 'Mama femenino y masculino, ovario/trompa/peritoneo, próstata y páncreas.', '<b>Vigilancia:</b> resonancia mamaria y mamografía según edad/gen. <b>Prevención:</b> considerar mastectomía y salpingooforectomía reductoras de riesgo. <b>Familiares:</b> prueba en cascada. <b>Ética:</b> consentimiento, confidencialidad, impacto psicológico y reproductivo.', 'Eje mama-ovario y defecto de recombinación homóloga.')

case('5. Caso 2: Síndrome de Lynch','Hombre de 45 años con cáncer colorrectal; padre con colon a los 50 y abuela materna con endometrio a los 55.','<b>Síndrome:</b> Lynch. <b>Herencia:</b> autosómica dominante.', ['Colon antes de los 50 años.','Colon y endometrio son tumores clásicos de Lynch.','El padre y la abuela materna pertenecen a ramas distintas: la genealogía debe analizarse por separado.','Aun así, el colon temprano justifica IHC/MSI tumoral.'], 'MLH1, MSH2, MSH6, PMS2 y EPCAM.', '<b>MSH2/MSH6</b> reconocen errores; <b>MLH1/PMS2</b> coordinan la reparación. <b>EPCAM no repara ADN</b>, pero algunas deleciones silencian MSH2.', 'IHC de proteínas MMR y/o MSI en tumor; después panel germinal por NGS con análisis de deleción/duplicación.', 'Colon, endometrio, ovario, estómago, intestino delgado, vías urinarias, páncreas, vías biliares, cerebro y tumores sebáceos.', '<b>Vigilancia:</b> colonoscopia frecuente y controles por órgano. <b>Prevención:</b> medidas ginecológicas individualizadas; aspirina según valoración médica. <b>Familiares:</b> prueba dirigida. <b>Ética:</b> explicar diferencia entre hallazgo tumoral y germinal.', 'Colon-endometrio sin cientos de pólipos; deficiencia MMR/MSI.')

case('6. Caso 3: Li-Fraumeni','Joven de 21 años con osteosarcoma; madre con mama a los 30 y abuelo materno con cáncer cerebral a los 40.','<b>Síndrome:</b> Li-Fraumeni. <b>Herencia:</b> autosómica dominante; puede ser de novo.', ['Osteosarcoma a edad muy temprana.','Cáncer de mama a los 30 años.','Tumor cerebral temprano en la misma rama.','Espectro clásico de tumores diversos y precoces.'], 'TP53.', '<b>TP53</b> codifica p53, el “guardián del genoma”. Detiene el ciclo celular, favorece reparación, senescencia o apoptosis. Su pérdida permite proliferación de células dañadas.', 'Secuenciación germinal de TP53 en panel o estudio dirigido, con análisis de CNV; valorar mosaicismo o hematopoyesis clonal si la fracción alélica es baja.', 'Sarcomas, mama premenopáusica, cerebro, carcinoma adrenocortical, leucemias y numerosos tumores sólidos.', '<b>Vigilancia:</b> resonancia corporal total, cerebral y controles específicos. <b>Prevención:</b> minimizar radiación ionizante cuando exista alternativa. <b>Familiares:</b> estudiar incluso menores porque la vigilancia comienza temprano. <b>Ética:</b> alto impacto psicológico.', 'Espectro multitumoral muy amplio y edades extremadamente tempranas.')

case('7. Caso 4: Cowden / PHTS','Mujer de 30 años con nódulos tiroideos y múltiples pápulas en cara y mucosas; madre con mama y abuela con tiroides.','<b>Síndrome:</b> Cowden, dentro de PTEN Hamartoma Tumor Syndrome. <b>Herencia:</b> autosómica dominante.', ['Pápulas faciales y mucosas típicas.','Nódulos tiroideos en persona joven.','Mama y tiroides en la misma rama.','Puede coexistir macrocefalia, pólipos y hamartomas.'], 'PTEN.', '<b>PTEN</b> es una fosfatasa supresora tumoral que inhibe PI3K/AKT/mTOR. Actúa como freno del crecimiento y supervivencia celular. Su pérdida favorece hamartomas y cáncer.', 'Panel germinal por NGS con análisis de deleción/duplicación de PTEN.', 'Mama, tiroides no medular, endometrio, riñón y colorrectal; además de lesiones benignas hamartomatosas.', '<b>Vigilancia:</b> ecografía tiroidea, mama, endometrio, riñón y colon según edad. <b>Prevención:</b> individualizada. <b>Familiares:</b> prueba dirigida. <b>Ética:</b> correlacionar el fenotipo; una pápula aislada no confirma el síndrome.', 'Hamartomas, lesiones mucocutáneas y eje mama-tiroides-endometrio.')

case('8. Caso 5: Poliposis Adenomatosa Familiar','Hombre de 25 años con hematoquecia y más de 100 pólipos adenomatosos; padre con cáncer colorrectal a los 35.','<b>Síndrome:</b> FAP clásica. <b>Herencia:</b> autosómica dominante; puede existir de novo o mosaicismo.', ['Más de 100 adenomas a los 25 años.','Cáncer colorrectal muy temprano en el padre.','Transmisión vertical compatible con autosómica dominante.','Riesgo colorrectal extremadamente alto sin intervención.'], 'APC; diferenciales: MUTYH, POLE, POLD1, NTHL1.', '<b>APC</b> integra el complejo que degrada beta-catenina. Cuando falla, beta-catenina se acumula y activa genes proliferativos. MUTYH suele producir poliposis autosómica recesiva.', 'Panel de poliposis por NGS con CNV de APC; si sangre negativa y fenotipo claro, evaluar mosaicismo mediante alta profundidad y/o tejido de pólipos.', 'Colorrectal, duodeno/ampolla, tiroides; también tumores desmoides y, en ciertos contextos, hepatoblastoma.', '<b>Vigilancia:</b> colon desde adolescencia y endoscopia alta. <b>Prevención:</b> colectomía cuando la carga de pólipos lo indique. <b>Familiares:</b> estudiar menores por beneficio médico. <b>Ética:</b> cirugía, imagen corporal, fertilidad y calidad de vida.', 'Poliposis adenomatosa masiva; a diferencia de Lynch, hay cientos o miles de pólipos.')

S += [P('9. Comparación final','H1x')]
rows=[['Síndrome','Gen/vía','Pista clínica','Tumores guía'],['HBOC','BRCA1/2 – recombinación homóloga','Mama joven + ovario','Mama, ovario, próstata, páncreas'],['Lynch','MMR','Colon + endometrio, pocos pólipos','Colon, endometrio y espectro Lynch'],['Li-Fraumeni','TP53','Sarcoma + cánceres muy precoces','Mama, sarcoma, cerebro, suprarrenal'],['Cowden/PHTS','PTEN – PI3K/AKT/mTOR','Pápulas, macrocefalia, tiroides','Mama, tiroides, endometrio, riñón'],['FAP','APC – Wnt/beta-catenina','Más de 100 adenomas','Colon, duodeno, tiroides']]
S += [tab(rows,[2.6*cm,4.1*cm,5.2*cm,5.7*cm],6.7),P('Diferencias que debes memorizar','H2x'),bul('<b>Lynch vs FAP:</b> Lynch tiene pocos pólipos y dMMR/MSI; FAP tiene cientos/miles de adenomas.'),bul('<b>HBOC vs Li-Fraumeni:</b> ambos pueden causar mama joven, pero Li-Fraumeni agrega sarcomas, cerebro y suprarrenal.'),bul('<b>HBOC vs Cowden:</b> Cowden añade pápulas, macrocefalia, hamartomas y tiroides.'),bul('<b>NGS vs MLPA:</b> NGS lee secuencia; MLPA cuantifica copias.'),bul('<b>IHC/MSI vs germinal:</b> IHC/MSI estudian el tumor; sangre/saliva confirma predisposición hereditaria.'),PageBreak()]

S += [P('10. Algoritmo rápido','H1x'),box('Reconocer el patrón','Mama-ovario → HBOC. Colon-endometrio sin poliposis → Lynch. Sarcoma y múltiples tumores precoces → Li-Fraumeni. Pápulas/hamartomas/tiroides → Cowden. Más de 100 adenomas → FAP.'),Spacer(1,.2*cm),box('Elegir la prueba','Varios genes posibles → panel NGS. Variante familiar conocida → prueba dirigida/Sanger. Deleción o duplicación → MLPA/CNV. Sospecha Lynch → IHC/MSI tumoral y confirmación germinal.'),Spacer(1,.2*cm),box('Interpretar','Patogénica o probablemente patogénica: accionable. VUS: no confirma y no debe guiar cirugía. Negativo: revisar cobertura, CNV, mosaicismo e historia familiar.',LR,RED),P('Mini repaso','H2x')]
rows=[['Pregunta','Respuesta'],['¿Quién repara roturas de doble cadena?','BRCA1/BRCA2'],['¿Quién corrige errores de apareamiento?','MLH1, MSH2, MSH6, PMS2'],['¿Guardián del genoma?','TP53'],['¿Inhibe PI3K/AKT/mTOR?','PTEN'],['¿Controla beta-catenina?','APC'],['¿Síndrome con cientos de adenomas?','FAP'],['¿Colon + endometrio?','Lynch'],['¿Pápulas + tiroides?','Cowden/PHTS'],['¿Qué detecta MLPA?','Deleciones/duplicaciones de exones'],['¿Qué variante no guía cirugía?','VUS']]
S += [tab(rows,[10.3*cm,7.3*cm],7.4),Spacer(1,.3*cm),P('<b>Nota:</b> material educativo. La vigilancia y prevención reales deben individualizarse con genética clínica y oncología.'),P('Actualizado para estudio: julio de 2026.','S')]

doc.build(S,onFirstPage=footer,onLaterPages=footer)
print(OUT)
