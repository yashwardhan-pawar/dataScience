  begin
    l := json_list();
    assertTrue(l.count = 0);
    pass(str);
  exception
    when others then fail(str);
  end;

  str := 'Empty list test and remove';
  declare
    l json_list;
  begin
    l := json_list();
    l.remove(3);
    l.remove_first;
    l.remove_last;
    assertTrue(l.count = 0);
    pass(str);
  exception
    when others then fail(str);
  end;

  str := 'Empty list test and add element';
  declare
    l json_list;
  begin
    l := json_list();
    l.append('MyElem');
    assertTrue(l.count = 1);
    pass(str);
  exception
    when others then fail(str);
  end;

  str := 'List parser constructor link test';
  declare
    l json_list; x number; obj json;
  begin
    l := json_list('[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]');
    begin
    assertTrue(15 = l.count);
    l := json_list('[1, [], {"nest":true}]');
    assertTrue(l.count = 3);
    assertTrue(1 = l.get(1).get_number);
    begin
    obj := json(l.get(3));
    assertTrue(obj.exist('nest'));
    assertTrue(obj.count = 1);
    end;

    begin
    obj := json(l.get(3));
    assertTrue(obj.exist('nest'));
    assertTrue(obj.count = 1);
    end;


    l := json_list(l.get(2));
    assertTrue(l.count = 0);
    end;
    pass(str);
  exception
    when others then fail(str);
  end;