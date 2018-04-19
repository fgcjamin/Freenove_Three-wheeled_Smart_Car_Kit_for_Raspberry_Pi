import inputs

cmds = set()
abs_dic = {}
while True:
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == "Absolute":
        #print(event.ev_type, event.code, event.state)
            stk = event.code
            val = event.state            
            if stk in abs_dic:
                if val >= 0 and abs_dic[stk][1] < val:
                    abs_dic[stk]=(abs_dic[stk][0],val)
                elif val < 0 and abs_dic[stk][0] > val:
                    abs_dic[stk]=(val,abs_dic[stk][1])
            else:                
                if val >= 0:
                    abs_dic[stk]=(0,val)
                else:
                    abs_dic[stk]=(val,0)
        #cmds.add(event.code)
    print("===========")
    print(abs_dic)    
    #for c in set(cmds):
    #    print(c)
