graph={
  'Biratnagar':{'Itahari':'22 KMs','Biratchowk':'30 KMs','Rangeli':'25 KMs'},
  'Itahari':{'Biratnagar':'22 KMs','Biratchowk':'11 KMs','Dharan':'20 KMs'},
  'Biratchowk':{'Itahari':'11 KMs','Kanepokhari':'10 KMs','Biratnagar':'30 KMs'},
  'Rangeli':{'Biratnagar':'25 KMs','Kanepokhari':'25 KMs','Urlabari':'40 KMs'},
  'Dharan':{'Itahari':'20 KMs'},
  'Kanepokhari':{'Biratchowk':'10 KMs','Rangeli':'25 KMs','Urlabari':'12 KMs'},
  'Urlabari':{'Damak':'6 KMs'}
}

for node in graph:
    print(f"{node} -> {graph[node]}")

print('The distance between Knaepokhari and Urlabari is',graph['Kanepokhari']['Urlabari'])