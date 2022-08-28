from lxml import etree

b2 = []


def das_dict():
    das = 'das.xml'
    doc = etree.parse(das)

    for l in doc.xpath('//Let'):
        b2.append(l.text)
        b2.append(l.attrib['Id'])


b = []


def from_latin_to_das(a):
    for i in a:
        if i == b2[0]:
            b.append(b2[1])
        elif i == b2[2]:
            b.append(b2[3])
        elif i == b2[4]:
            b.append(b2[5])
        elif i == b2[6]:
            b.append(b2[7])
        elif i == b2[8]:
            b.append(b2[9])
        elif i == b2[10]:
            b.append(b2[11])
        elif i == b2[12]:
            b.append(b2[13])
        elif i == b2[14]:
            b.append(b2[15])
        elif i == b2[16]:
            b.append(b2[17])
        elif i == b2[18]:
            b.append(b2[19])
        elif i == b2[20]:
            b.append(b2[21])
        elif i == b2[22]:
            b.append(b2[23])
        elif i == b2[24]:
            b.append(b2[25])
        elif i == b2[26]:
            b.append(b2[27])
        elif i == b2[28]:
            b.append(b2[29])
        elif i == b2[30]:
            b.append(b2[31])
        elif i == b2[32]:
            b.append(b2[33])
        elif i == b2[34]:
            b.append(b2[35])
        elif i == b2[36]:
            b.append(b2[37])
        elif i == b2[38]:
            b.append(b2[39])
        elif i == b2[40]:
            b.append(b2[41])
        elif i == b2[42]:
            b.append(b2[43])
        elif i == b2[44]:
            b.append(b2[45])
        elif i == b2[46]:
            b.append(b2[47])
        elif i == b2[48]:
            b.append(b2[49])
        elif i == b2[50]:
            b.append(b2[51])
    print(''.join(b))


def from_das_to_latin(n):
    for i in n:
        if i == b2[1]:
            b.append(b2[0])
        elif i == b2[3]:
            b.append(b2[2])
        elif i == b2[5]:
            b.append(b2[4])
        elif i == b2[7]:
            b.append(b2[6])
        elif i == b2[9]:
            b.append(b2[8])
        elif i == b2[11]:
            b.append(b2[10])
        elif i == b2[13]:
            b.append(b2[12])
        elif i == b2[15]:
            b.append(b2[14])
        elif i == b2[17]:
            b.append(b2[16])
        elif i == b2[19]:
            b.append(b2[18])
        elif i == b2[21]:
            b.append(b2[20])
        elif i == b2[23]:
            b.append(b2[22])
        elif i == b2[25]:
            b.append(b2[24])
        elif i == b2[27]:
            b.append(b2[26])
        elif i == b2[29]:
            b.append(b2[28])
        elif i == b2[31]:
            b.append(b2[30])
        elif i == b2[33]:
            b.append(b2[32])
        elif i == b2[35]:
            b.append(b2[34])
        elif i == b2[37]:
            b.append(b2[36])
        elif i == b2[39]:
            b.append(b2[38])
        elif i == b2[41]:
            b.append(b2[40])
        elif i == b2[43]:
            b.append(b2[42])
        elif i == b2[45]:
            b.append(b2[44])
        elif i == b2[47]:
            b.append(b2[46])
        elif i == b2[49]:
            b.append(b2[48])
        elif i == b2[51]:
            b.append(b2[50])
    print(''.join(b))


enter = input('Choose translate, to latin or to das\n'
              'Press to l or d: ')
if enter == 'd' or enter == 'D':
    das_dict()
    from_latin_to_das(a=input("Enter: ").casefold())
elif enter == 'l' or enter == 'L':
    das_dict()
    from_das_to_latin(n=input("Enter: "))
