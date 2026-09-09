"""
核融合のQ値をPythonで計算する｜「エネルギー収支」で実用性を測る

元記事: https://fusion.yurufuwa.work/learn/q-value-python
ゆるふわ核融合・次世代エネルギー (fusion.yurufuwa.work) の解説記事から抜粋したコードです。
"""

def q_value(energy_out, energy_in):
    return energy_out / energy_in

def status(Q):
    if Q < 1:    return "赤字（投入>出力）"
    if Q < 10:   return "科学的には成功、実用にはまだ"
    return "実用発電の目安を達成"

for out, inp, label in [
    (0.5, 1.0, "初期の実験"),
    (1.5, 1.0, "ブレークイーブン超え"),
    (500, 50,  "ITER目標クラス"),
]:
    Q = q_value(out, inp)
    print(f"{label}: Q = {Q:.1f} … {status(Q)}")

def engineering_q(fusion_out, laser_energy, wall_plug_efficiency=0.01):
    grid_energy = laser_energy / wall_plug_efficiency   # 壁のコンセントから見た投入
    return fusion_out / grid_energy

# 核融合出力3MJ、レーザー投入2MJ、装置効率1%の例
scientific = q_value(3.0, 2.0)
engineering = engineering_q(3.0, 2.0)
print(f"科学的Q: {scientific:.2f}")
print(f"工学的Q（施設全体）: {engineering:.4f}")
