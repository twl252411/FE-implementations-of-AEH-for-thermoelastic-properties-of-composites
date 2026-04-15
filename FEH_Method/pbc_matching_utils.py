from itertools import product


def build_periodic_set_lines(
    ndcord,
    NdRS,
    NdLS,
    NdTS,
    NdDS,
    NdFS,
    NdBS,
    NdEdAB,
    NdEdBC,
    NdEdCD,
    NdEdDA,
    NdEdA1B1,
    NdEdB1C1,
    NdEdC1D1,
    NdEdD1A1,
    NdEdAA1,
    NdEdBB1,
    NdEdCC1,
    NdEdDD1,
    tol=1.0e-4,
    instance_name="Part-1-1",
):
    """Build all surface/edge periodic node-set lines with tolerant matching."""

    def _key(*vals):
        return tuple(int(round(v / tol)) for v in vals)

    neighbor_offsets = {
        1: [(-1,), (0,), (1,)],
        2: list(product([-1, 0, 1], repeat=2)),
    }

    def _build_index(nodes, axes):
        node_map, order_map = {}, {}
        for idx, jnd in enumerate(nodes):
            order_map[jnd] = idx
            key = _key(*[ndcord[jnd - 1, iax] for iax in axes])
            node_map.setdefault(key, []).append(jnd)
        return node_map, order_map

    def _find_match(nodes, axes, node_map, order_map, values):
        base_key = _key(*values)
        best_nd, best_idx = None, None
        for offset in neighbor_offsets[len(axes)]:
            near_key = tuple(base_key[ii] + offset[ii] for ii in range(len(axes)))
            for cand in node_map.get(near_key, []):
                if all(abs(ndcord[cand - 1, iax] - val) < tol for iax, val in zip(axes, values)):
                    cand_idx = order_map[cand]
                    if best_idx is None or cand_idx < best_idx:
                        best_nd, best_idx = cand, cand_idx
        if best_nd is not None:
            return best_nd
        for cand in nodes:
            if all(abs(ndcord[cand - 1, iax] - val) < tol for iax, val in zip(axes, values)):
                return cand
        return None

    addlnsS1, addlnsS2, addlnsS15, addlnsS16, addlnsS18, addlnsS19 = [], [], [], [], [], []
    ssetnum1, ssetnum2, ssetnum3 = 0, 0, 0

    ls_map, ls_order = _build_index(NdLS, (2, 3))
    ds_map, ds_order = _build_index(NdDS, (1, 3))
    bs_map, bs_order = _build_index(NdBS, (2, 1))

    for ind in NdRS:
        ssetnum1 += 1
        addlnsS18.append(f"*Nset, nset=Set-RightSurf-{ssetnum1}, instance={instance_name}\n")
        addlnsS18.append(f" {ind},\n")
        jnd = _find_match(NdLS, (2, 3), ls_map, ls_order, (ndcord[ind - 1, 2], ndcord[ind - 1, 3]))
        if jnd is not None:
            addlnsS16.append(f"*Nset, nset=Set-LeftSurf-{ssetnum1}, instance={instance_name}\n")
            addlnsS16.append(f" {jnd},\n")

    for ind in NdTS:
        ssetnum2 += 1
        addlnsS19.append(f"*Nset, nset=Set-TopSurf-{ssetnum2}, instance={instance_name}\n")
        addlnsS19.append(f" {ind},\n")
        jnd = _find_match(NdDS, (1, 3), ds_map, ds_order, (ndcord[ind - 1, 1], ndcord[ind - 1, 3]))
        if jnd is not None:
            addlnsS2.append(f"*Nset, nset=Set-DownSurf-{ssetnum2}, instance={instance_name}\n")
            addlnsS2.append(f" {jnd},\n")

    for ind in NdFS:
        ssetnum3 += 1
        addlnsS15.append(f"*Nset, nset=Set-FrontSurf-{ssetnum3}, instance={instance_name}\n")
        addlnsS15.append(f" {ind},\n")
        jnd = _find_match(NdBS, (2, 1), bs_map, bs_order, (ndcord[ind - 1, 2], ndcord[ind - 1, 1]))
        if jnd is not None:
            addlnsS1.append(f"*Nset, nset=Set-BackSurf-{ssetnum3}, instance={instance_name}\n")
            addlnsS1.append(f" {jnd},\n")

    addlnsE3, addlnsE4, addlnsE5, addlnsE6, addlnsE7, addlnsE8 = [], [], [], [], [], []
    addlnsE9, addlnsE10, addlnsE11, addlnsE12, addlnsE13, addlnsE14 = [], [], [], [], [], []
    esetnum1, esetnum2, esetnum3 = 0, 0, 0

    edcd_map, edcd_order = _build_index(NdEdCD, (1,))
    edc1d1_map, edc1d1_order = _build_index(NdEdC1D1, (1,))
    eda1b1_map, eda1b1_order = _build_index(NdEdA1B1, (1,))

    edda_map, edda_order = _build_index(NdEdDA, (3,))
    edb1c1_map, edb1c1_order = _build_index(NdEdB1C1, (3,))
    edd1a1_map, edd1a1_order = _build_index(NdEdD1A1, (3,))

    edaa1_map, edaa1_order = _build_index(NdEdAA1, (2,))
    edcc1_map, edcc1_order = _build_index(NdEdCC1, (2,))
    eddd1_map, eddd1_order = _build_index(NdEdDD1, (2,))

    for ind in NdEdAB:
        esetnum1 += 1
        addlnsE5.append(f"*Nset, nset=Set-EdgeAB-{esetnum1}, instance={instance_name}\n")
        addlnsE5.append(f" {ind},\n")
        jnd = _find_match(NdEdCD, (1,), edcd_map, edcd_order, (ndcord[ind - 1, 1],))
        if jnd is not None:
            addlnsE11.append(f"*Nset, nset=Set-EdgeCD-{esetnum1}, instance={instance_name}\n")
            addlnsE11.append(f" {jnd},\n")
        knd = _find_match(NdEdC1D1, (1,), edc1d1_map, edc1d1_order, (ndcord[ind - 1, 1],))
        if knd is not None:
            addlnsE9.append(f"*Nset, nset=Set-EdgeC1D1-{esetnum1}, instance={instance_name}\n")
            addlnsE9.append(f" {knd},\n")
        lnd = _find_match(NdEdA1B1, (1,), eda1b1_map, eda1b1_order, (ndcord[ind - 1, 1],))
        if lnd is not None:
            addlnsE3.append(f"*Nset, nset=Set-EdgeA1B1-{esetnum1}, instance={instance_name}\n")
            addlnsE3.append(f" {lnd},\n")

    for ind in NdEdBC:
        esetnum2 += 1
        addlnsE8.append(f"*Nset, nset=Set-EdgeBC-{esetnum2}, instance={instance_name}\n")
        addlnsE8.append(f" {ind},\n")
        jnd = _find_match(NdEdDA, (3,), edda_map, edda_order, (ndcord[ind - 1, 3],))
        if jnd is not None:
            addlnsE13.append(f"*Nset, nset=Set-EdgeDA-{esetnum2}, instance={instance_name}\n")
            addlnsE13.append(f" {jnd},\n")
        knd = _find_match(NdEdB1C1, (3,), edb1c1_map, edb1c1_order, (ndcord[ind - 1, 3],))
        if knd is not None:
            addlnsE6.append(f"*Nset, nset=Set-EdgeB1C1-{esetnum2}, instance={instance_name}\n")
            addlnsE6.append(f" {knd},\n")
        lnd = _find_match(NdEdD1A1, (3,), edd1a1_map, edd1a1_order, (ndcord[ind - 1, 3],))
        if lnd is not None:
            addlnsE12.append(f"*Nset, nset=Set-EdgeD1A1-{esetnum2}, instance={instance_name}\n")
            addlnsE12.append(f" {lnd},\n")

    for ind in NdEdBB1:
        esetnum3 += 1
        addlnsE7.append(f"*Nset, nset=Set-EdgeBB1-{esetnum3}, instance={instance_name}\n")
        addlnsE7.append(f" {ind},\n")
        jnd = _find_match(NdEdAA1, (2,), edaa1_map, edaa1_order, (ndcord[ind - 1, 2],))
        if jnd is not None:
            addlnsE4.append(f"*Nset, nset=Set-EdgeAA1-{esetnum3}, instance={instance_name}\n")
            addlnsE4.append(f" {jnd},\n")
        knd = _find_match(NdEdCC1, (2,), edcc1_map, edcc1_order, (ndcord[ind - 1, 2],))
        if knd is not None:
            addlnsE10.append(f"*Nset, nset=Set-EdgeCC1-{esetnum3}, instance={instance_name}\n")
            addlnsE10.append(f" {knd},\n")
        lnd = _find_match(NdEdDD1, (2,), eddd1_map, eddd1_order, (ndcord[ind - 1, 2],))
        if lnd is not None:
            addlnsE14.append(f"*Nset, nset=Set-EdgeDD1-{esetnum3}, instance={instance_name}\n")
            addlnsE14.append(f" {lnd},\n")

    return (
        addlnsS1,
        addlnsS2,
        addlnsS15,
        addlnsS16,
        addlnsS18,
        addlnsS19,
        addlnsE3,
        addlnsE4,
        addlnsE5,
        addlnsE6,
        addlnsE7,
        addlnsE8,
        addlnsE9,
        addlnsE10,
        addlnsE11,
        addlnsE12,
        addlnsE13,
        addlnsE14,
    )
