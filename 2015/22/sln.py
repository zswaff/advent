#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


player_hp_init = 50
mana_init = 500
boss_hp_init = 55
boss_dmg_init = 8


def fmt_entry(is_player, player_hp, armor, mana, boss_hp, fx, action):
    char = "Player" if is_player else "Boss"
    title = f"- {char} -"
    pm = f"Player: h={player_hp} a={armor} m={mana}"
    bm = f"Boss: h={boss_hp}"
    fxm = f"Effects: {fx}"
    am = f"Action: {char} does {action}"
    return ["\n".join([title, pm, bm, fxm, am])]


def get_fx(fx):
    fx_n = dict(fx.items())
    armor = dmg_fx = mana_heal = 0
    for f, t in fx.items():
        if t == 0:
            continue
        if f == "shield":
            armor = 7
        if f == "poison":
            dmg_fx = 3
        if f == "recharge":
            mana_heal = 101
        fx_n[f] = fx[f] - 1
    return fx_n, armor, dmg_fx, mana_heal


def player_turn(player_hp, mana, boss_hp, fx, msgs, cost_in):
    global best_overall

    player_hp_after_loss = player_hp - player_hp_loss

    if player_hp_after_loss <= 0:
        return math.inf, []

    fx_after_fx, armor, dmg_fx, mana_heal = get_fx(fx)
    msgs_after_fx = msgs + fmt_entry(True, player_hp, armor, mana, boss_hp, fx, "nothing")
    boss_hp_after_fx = boss_hp - dmg_fx
    mana_after_fx = mana + mana_heal

    if boss_hp_after_fx <= 0:
        best_overall = min(best_overall, cost_in)
        return 0, msgs_after_fx

    best = math.inf, []
    for action in ["missile", "drain", "shield", "poison", "recharge"]:
        if fx_after_fx.get(action, 0) > 0:
            continue

        fx_after_action = dict(fx_after_fx.items())
        mana_cost = dmg_action = heal = 0
        if action == "missile":
            mana_cost = 53
            dmg_action = 4
        if action == "drain":
            mana_cost = 73
            dmg_action = 2
            heal = 2
        if action == "shield":
            mana_cost = 113
            fx_after_action[action] = 6
        if action == "poison":
            mana_cost = 173
            fx_after_action[action] = 6
        if action == "recharge":
            mana_cost = 229
            fx_after_action[action] = 5

        msgs_after_action = msgs + fmt_entry(True, player_hp, armor, mana, boss_hp, fx, action)
        player_hp_after_action = player_hp_after_loss + heal
        mana_after_action = mana_after_fx - mana_cost
        boss_hp_after_action = boss_hp_after_fx - dmg_action
        cost_out = cost_in + mana_cost

        if mana_after_action < 0:
            continue

        if cost_out > best_overall:
            continue

        if boss_hp_after_action <= 0:
            best = min(best, (mana_cost, msgs_after_action))
            continue

        mana_cost_rec, msgs_rec = boss_turn(
            player_hp_after_action,
            mana_after_action,
            boss_hp_after_action,
            fx_after_action,
            msgs_after_action,
            cost_out,
        )
        mana_cost_total = mana_cost + mana_cost_rec
        best = min(best, (mana_cost_total, msgs_rec))
    return best


def boss_turn(player_hp, mana, boss_hp, fx, msgs, cost_in):
    global best_overall

    fx_after_fx, armor, dmg_fx, mana_heal = get_fx(fx)
    msgs_after_fx = msgs + fmt_entry(False, player_hp, armor, mana, boss_hp, fx, "nothing")
    boss_hp_after_fx = boss_hp - dmg_fx
    mana_after_fx = mana + mana_heal

    if boss_hp_after_fx <= 0:
        best_overall = min(best_overall, cost_in)
        return 0, msgs_after_fx

    boss_dmg = max(boss_dmg_init - armor, 1)

    msgs_after_action = msgs + fmt_entry(False, player_hp, armor, mana, boss_hp, fx, "attack")
    player_hp_after_action = player_hp - boss_dmg

    if player_hp_after_action <= 0:
        return math.inf, []

    return player_turn(
        player_hp_after_action,
        mana_after_fx,
        boss_hp_after_fx,
        fx_after_fx,
        msgs_after_action,
        cost_in,
    )


# part 2
best_overall = math.inf
player_hp_loss = 0
cost_f, _ = player_turn(player_hp_init, mana_init, boss_hp_init, {}, [], 0)
print(cost_f)


# part 2
best_overall = math.inf
player_hp_loss = 1
cost_f, _ = player_turn(player_hp_init, mana_init, boss_hp_init, {}, [], 0)
print(cost_f)
