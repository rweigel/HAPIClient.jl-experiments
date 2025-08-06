using Pkg
packages = [ p.name for p in values(Pkg.dependencies()) ]
if !("Plots" in packages)
  Pkg.add("Plots")
end

using Plots
using HAPIClient

if isfile("scripts.bin")
  using Serialization
  println("Reading scripts.bin")
  data = open("scripts.bin", "r") do io
      deserialize(io)
  end
else
  println("Binary file 'scripts.bin' does not exist. Run scripts.jl to create it.")
end

plot(data[1].time, data[1].values, label=data[1].meta["name"])
savefig("scripts.png")