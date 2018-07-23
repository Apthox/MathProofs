import wolframalpha

client = wolframalpha.Client("RRRLTV-GPJLHPE2A4")

request = "solve " \
          "(-dX) - (cY(X / (1 + X))) + ((e^(-k * H))j(X / (1 + X))) + (l(X / (1 + X))Z)" \
          " and " \
          "(-gW) - (gY(W / (1 + W))) + (c(e^(-k * H))h(W / (1 + W))) + (f(W / (1 + W))Z)" \
          " and " \
          "(-aY) + ((bX)(Y / (Y + 1))(1 - (Y / n))) + ((p(1 / e^(-k * H)))(Y / (Y + 1)))" \
          " and " \
          "(lX) + (fW) - (mZ)"

res = client.query(request)

print(str(res))