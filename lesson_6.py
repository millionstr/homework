"""
1. Визначити, який відсоток слів у тексті починається з букви “z”.
2. Знайти довжину самого короткого слова
3. Визначити на яку букву починається більшість слів у заданому тексті
4. У заданому тексті знищити всі слова з парними порядковими номерами.
5. У заданому тексті поміняти місцями перше й останнє слова.
"""
text = """Etiam in porta mauris, ut lacinia dui. Suspendisse maximus ipsum purus, vitae cursus mauris blandit eu. Integer tempor non neque eget eleifend. Morbi id nulla nec lectus lobortis imperdiet eget mollis enim. Donec sed quam a mi maximus suscipit lacinia vel sapien. Vivamus dolor nisl, interdum eget porttitor in, malesuada ut mi. Nam ac fermentum velit, non gravida sem. Nullam ante leo, volutpat vel sapien  nec,  dignissimfaucibus  lacus.  Proin  sed  ligula  vitae  est  porttitor  vulputate  convallis  sed  mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent viverra, ante eget ultricies venenatis, nulla mauris euismod velit, vitae pretium neque massa at nunc. Nullaid dictum nunc. Integer efficitur dictum  felis  sed  maximus.  Cras  ultrices  erat  vitae  mauris  rhoncus  blandit.  Morbi  ultrices  at  elit  vel dignissim. Etiam libero risus, mattis iaculis magna ac, egestas varius odio.Nam  viverra  quam  id  purus  pulvinar,  ac  interdum  diam  tincidunt.  In  pulvinar  nibh  sit  amet  purus dignissim, et porttitor libero dapibus. Nunc non nisi vel mi iaculis placerat. Proin porttitor sapien dui, at tempor dolor egestas ac. Phasellus eleifend tellus eu mauris dictum sollicitudin ac ut quam.Aliquam auctor erat vitae diam bibendum feugiat. Mauris ut dolor id ante feugiat lobortis. Duis in quam cursus, tincidunt lorem at, sagittis libero. Mauris tortor nisi, efficitur sit amet sapien sit amet, ultrices lacinia mi. Nulla  facilisi.  Nullam  laoreet  tortor id  ante  interdum,  non  tempus  ante  gravida.  Integer  nec  volutpat odio, vitae ullamcorper est. Etiam ligula dui, convallis et blandit vitae, varius vitae mauris. Mauris vitae pellentesque  justo,  a  ullamcorper  metus.  Maecenas  porttitor  massa  vitae  tortor  interdum,  aliquam rutrum tellus tincidunt.Sed vehicula felis a leo tempus, in fermentum turpis elementum. Pellentesque non sodales nulla, eget efficitur neque. In hac habitasse platea dictumst. Vivamus nec ultrices est. Fusce ac erat sed lectus egestas  consequat.  Sed  scelerisque  nisi  sem,  ut  dictum  diam  efficitur  laoreet.  Integer  aliquam  in mauris in varius. Sed eget tempus ex. Praesent nec neque eu erat dapibus lacinia id quis nulla. Praesent  quam  diam,  volutpat  at  velit  sed,  ultricies  tincidunt  nunc.  Etiam  metus  lorem,  rutrum  et sollicitudin eget, dictum feugiat augue. Sed quis libero at turpis lobortis gravida. Nunc congue eget ipsum eget euismod. Cras odio nulla, sollicitudin imperdiet diam vel, pellentesque congue nunc. Nunc a odio eu mauris blandit placerat at sit amet turpis. Donec eget mattis felis. Sed dui odio, tincidunt eget ullamcorper non, ornare eget libero. Morbi eu lorem bibendum, pharetra sem id, condimentum mauris. Integer  volutpat  pharetra  mauris  ut  hendrerit.  Interdum  et  malesuada  fames  ac  ante ipsum primis in faucibus."""

a=ord('a')#сворюємо список символів з яких складаються слова
z=ord('z')
A=ord('A')
Z=ord('Z')
az=list()
AZ=list()
for i in range(a,z+1):
    az.append(chr(i))
for i in range(A,Z+1):
    AZ.append(chr(i))  
print(az,AZ)
azAZ= az + AZ
print(azAZ)

slovo=list()#ствоюємо список в якому буде список тільки слів, без знаків пуктуації
lists=list()
for i in text:
    if i in azAZ:
        slovo.append(i)
    else:
        if slovo:
            #print(slovo)
            lists.append(slovo)
        slovo=list()
print(lists, len(lists))

# визначаємо скільки відсотків слів починається з заданої літери
char_seach = input("введіть букву з якої починається слово: ")
kilkist=0
for i in lists:
    if i[0]==char_seach:
        kilkist+=1
print(f"{kilkist/len(lists)*100:.2f} відсотків слів починаються на букву <{char_seach}>")

# визначаємо довжину найкоротшого слова в тексті
len_min_slova=len(lists[0])
for i in lists:
    if len(i)<len_min_slova:
        len_min_slova=len(i)
        #print(i)
print(f"довжина самого короткого слова {len_min_slova}")

# Визначити на яку букву починається більшість слів у заданому тексті
def repeat_letters(letter,lists):
    kilkist=0
    for i in lists:
        if i[0]==letter:
            kilkist+=1
    return (kilkist/len(lists)*100)

max_letter=['a',0]
for i in azAZ:
    RL = repeat_letters(i, lists)
    if max_letter[1] < RL:
        max_letter[1]=RL
        max_letter[0]=i

print(f"найчастіше зустрічається літера {max_letter[0]} , {max_letter[1]:.2f} відсотків")

# У заданому тексті знищити всі слова з парними порядковими номерами
amount = len(lists)-1
print(amount,' = amount')
for i in range(amount,0,-2):
    #print(i, " ",lists[i])
    lists.pop(i)
print(len(lists),' після знищення з парним номером')

#  У заданому тексті поміняти місцями перше й останнє слова
amount1 = len(lists)-1
lists[0], lists[amount1] = lists[amount1], lists[0]
