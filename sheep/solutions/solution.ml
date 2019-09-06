let sheep x =
  let rec sheep x i = match x with
  | x when i = x -> (Printf.printf "%d sheep... " x)
  | z -> (Printf.printf "%d sheep... " x; sheep (x+1) i)
  in sheep 1 x
in sheep (read_int ())

