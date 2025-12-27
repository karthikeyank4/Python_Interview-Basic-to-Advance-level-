#Dictionary is one of the Datatype in Python , It's Key -Value pair .

dic={"a":"apple","b":"Ball"}
print(dic)

print(dic["a"]  )
dic["a"]="Ajith"
print(dic)
del dic["b"]
print(dic)
dic.update({"c" :"Cat" ,"d":"Dog"})
print(dic['d'])
dic.pop("d")
print(dic)

#Update, deletion
# dic.insert[{"c":"lCat"}]
# print(dic)
# constructor , methods, read & write , inheritance , strings