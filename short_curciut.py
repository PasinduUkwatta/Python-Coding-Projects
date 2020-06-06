#Short Circuiting

is_friend = True
is_human=True

#this is short curcuting , becuse in this interpreter only look in the first agumnet . it dont consider abut the second one beacuse in the or operator on true is enough for become true. 
if (is_friend or is_human):
  print('A Good Friend')