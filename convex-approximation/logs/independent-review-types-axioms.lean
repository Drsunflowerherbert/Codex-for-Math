import ConvexApprox
set_option pp.universes true
set_option pp.explicit true

#check @ConvexApprox.supportBarrier
#print axioms ConvexApprox.supportBarrier
#check @ConvexApprox.supportBarrier_eq_sum
#print axioms ConvexApprox.supportBarrier_eq_sum
#check @ConvexApprox.supportBarrier_eq_barrier
#print axioms ConvexApprox.supportBarrier_eq_barrier
#check @ConvexApprox.contDiff_supportBarrier
#print axioms ConvexApprox.contDiff_supportBarrier
#check @ConvexApprox.supportBarrier_halfspace
#print axioms ConvexApprox.supportBarrier_halfspace
#check @ConvexApprox.supportBarrier_lt_one
#print axioms ConvexApprox.supportBarrier_lt_one
#check @ConvexApprox.net_positive_cover
#print axioms ConvexApprox.net_positive_cover
#check @ConvexApprox.supportValue_sub_inner_le_diam
#print axioms ConvexApprox.supportValue_sub_inner_le_diam
#check @ConvexApprox.exp_lower_supportBarrier
#print axioms ConvexApprox.exp_lower_supportBarrier
#check @ConvexApprox.isCompact_supportBarrier_sublevel
#print axioms ConvexApprox.isCompact_supportBarrier_sublevel
#check @ConvexApprox.tendsto_supportBarrier_atTop
#print axioms ConvexApprox.tendsto_supportBarrier_atTop
#check @ConvexApprox.supportBarrier_inner_tube
#print axioms ConvexApprox.supportBarrier_inner_tube
#check @ConvexApprox.strictConvexOn_supportBarrier
#print axioms ConvexApprox.strictConvexOn_supportBarrier
#check @ConvexApprox.supportBarrier_outer_error
#print axioms ConvexApprox.supportBarrier_outer_error
#check @ConvexApprox.supportBarrier_hausdorff_error
#print axioms ConvexApprox.supportBarrier_hausdorff_error
#check @ConvexApprox.closure_supportBarrier_lt
#print axioms ConvexApprox.closure_supportBarrier_lt
#check @ConvexApprox.frontier_supportBarrier_lt
#print axioms ConvexApprox.frontier_supportBarrier_lt
#check @ConvexApprox.fderiv_supportBarrier_ne_zero
#print axioms ConvexApprox.fderiv_supportBarrier_ne_zero
#check @ConvexApprox.supportBarrier_certified_nesting
#print axioms ConvexApprox.supportBarrier_certified_nesting
#check @ConvexApprox.supportBarrier_hessian_pos
#print axioms ConvexApprox.supportBarrier_hessian_pos
#check @ConvexApprox.supportBarrier_outer_approximation
#print axioms ConvexApprox.supportBarrier_outer_approximation
#check @ConvexApprox.supportBarrier_open_chord
#print axioms ConvexApprox.supportBarrier_open_chord
#check @ConvexApprox.strictConvex_supportBarrier_closed
#print axioms ConvexApprox.strictConvex_supportBarrier_closed
#check @ConvexApprox.convex_supportBarrier_open
#print axioms ConvexApprox.convex_supportBarrier_open
#check @ConvexApprox.barrier
#print axioms ConvexApprox.barrier
#check @ConvexApprox.barrierDeriv
#print axioms ConvexApprox.barrierDeriv
#check @ConvexApprox.barrierHessian
#print axioms ConvexApprox.barrierHessian
#check @ConvexApprox.hasFDerivAt_barrier
#print axioms ConvexApprox.hasFDerivAt_barrier
#check @ConvexApprox.hasFDerivAt_barrierDeriv
#print axioms ConvexApprox.hasFDerivAt_barrierDeriv
#check @ConvexApprox.fderiv_barrier
#print axioms ConvexApprox.fderiv_barrier
#check @ConvexApprox.fderiv_barrierDeriv
#print axioms ConvexApprox.fderiv_barrierDeriv
#check @ConvexApprox.barrierDeriv_apply
#print axioms ConvexApprox.barrierDeriv_apply
#check @ConvexApprox.barrierHessian_apply
#print axioms ConvexApprox.barrierHessian_apply
#check @ConvexApprox.barrierHessian_diag
#print axioms ConvexApprox.barrierHessian_diag
#check @ConvexApprox.contDiff_barrier
#print axioms ConvexApprox.contDiff_barrier
#check @ConvexApprox.fderiv_fderiv_barrier
#print axioms ConvexApprox.fderiv_fderiv_barrier
#check @ConvexApprox.barrierHessian_symmetric
#print axioms ConvexApprox.barrierHessian_symmetric
#check @ConvexApprox.barrierHessian_nonneg
#print axioms ConvexApprox.barrierHessian_nonneg
#check @ConvexApprox.barrierHessian_pos_of_exists
#print axioms ConvexApprox.barrierHessian_pos_of_exists
#check @ConvexApprox.barrierHessian_pos
#print axioms ConvexApprox.barrierHessian_pos
#check @ConvexApprox.affineCombination
#print axioms ConvexApprox.affineCombination
#check @ConvexApprox.convexOn_barrier
#print axioms ConvexApprox.convexOn_barrier
#check @ConvexApprox.strictConvexOn_barrier
#print axioms ConvexApprox.strictConvexOn_barrier
#check @ConvexApprox.barrier_supporting
#print axioms ConvexApprox.barrier_supporting
#check @ConvexApprox.barrierDeriv_apply_pos_of_level
#print axioms ConvexApprox.barrierDeriv_apply_pos_of_level
#check @ConvexApprox.barrierDeriv_ne_zero_of_level
#print axioms ConvexApprox.barrierDeriv_ne_zero_of_level
#check @ConvexApprox.closure_barrier_lt
#print axioms ConvexApprox.closure_barrier_lt
#check @ConvexApprox.frontier_barrier_lt
#print axioms ConvexApprox.frontier_barrier_lt
#check @ConvexApprox.exists_outer_parameters_containing
#print axioms ConvexApprox.exists_outer_parameters_containing
#check @ConvexApprox.Examples.horizontal
#print axioms ConvexApprox.Examples.horizontal
#check @ConvexApprox.Examples.vertical
#print axioms ConvexApprox.Examples.vertical
#check @ConvexApprox.Examples.planarSegment
#print axioms ConvexApprox.Examples.planarSegment
#check @ConvexApprox.Examples.horizontal_norm
#print axioms ConvexApprox.Examples.horizontal_norm
#check @ConvexApprox.Examples.vertical_norm
#print axioms ConvexApprox.Examples.vertical_norm
#check @ConvexApprox.Examples.planarAxes
#print axioms ConvexApprox.Examples.planarAxes
#check @ConvexApprox.Examples.planarAxes_unit
#print axioms ConvexApprox.Examples.planarAxes_unit
#check @ConvexApprox.Examples.exists_planarNet
#print axioms ConvexApprox.Examples.exists_planarNet
#check @ConvexApprox.Examples.planarSegment_nonempty
#print axioms ConvexApprox.Examples.planarSegment_nonempty
#check @ConvexApprox.Examples.planarSegment_compact
#print axioms ConvexApprox.Examples.planarSegment_compact
#check @ConvexApprox.Examples.planarSegment_convex
#print axioms ConvexApprox.Examples.planarSegment_convex
#check @ConvexApprox.Examples.planarSegment_eq_image
#print axioms ConvexApprox.Examples.planarSegment_eq_image
#check @ConvexApprox.Examples.horizontal_mem_planarSegment
#print axioms ConvexApprox.Examples.horizontal_mem_planarSegment
#check @ConvexApprox.Examples.horizontal_ne_zero
#print axioms ConvexApprox.Examples.horizontal_ne_zero
#check @ConvexApprox.Examples.planarSegment_diam
#print axioms ConvexApprox.Examples.planarSegment_diam
#check @ConvexApprox.Examples.planarSegment_vertical_zero
#print axioms ConvexApprox.Examples.planarSegment_vertical_zero
#check @ConvexApprox.Examples.planarSegment_interior_empty
#print axioms ConvexApprox.Examples.planarSegment_interior_empty
#check @ConvexApprox.Examples.planarSegment_infDist_le_exact_outer_error
#print axioms ConvexApprox.Examples.planarSegment_infDist_le_exact_outer_error
#check @ConvexApprox.Examples.planarSingleton_norm_le_outer_error
#print axioms ConvexApprox.Examples.planarSingleton_norm_le_outer_error
#check @ConvexApprox.Examples.planarSegment_barrier_compact
#print axioms ConvexApprox.Examples.planarSegment_barrier_compact
#check @ConvexApprox.Examples.planarSegment_barrier_lt_one
#print axioms ConvexApprox.Examples.planarSegment_barrier_lt_one
#check @ConvexApprox.Examples.planarSegment_barrier_hausdorff_error
#print axioms ConvexApprox.Examples.planarSegment_barrier_hausdorff_error
#check @ConvexApprox.Examples.planarSingleton_barrier_radius
#print axioms ConvexApprox.Examples.planarSingleton_barrier_radius
#check @ConvexApprox.IsChordalNet
#print axioms ConvexApprox.IsChordalNet
#check @ConvexApprox.supportValue
#print axioms ConvexApprox.supportValue
#check @ConvexApprox.exists_support_maximizer
#print axioms ConvexApprox.exists_support_maximizer
#check @ConvexApprox.exists_supportValue_eq
#print axioms ConvexApprox.exists_supportValue_eq
#check @ConvexApprox.inner_le_supportValue
#print axioms ConvexApprox.inner_le_supportValue
#check @ConvexApprox.nearest_point_normal
#print axioms ConvexApprox.nearest_point_normal
#check @ConvexApprox.exists_chordalNet_containing
#print axioms ConvexApprox.exists_chordalNet_containing
#check @ConvexApprox.IsChordalNet.exists_inner_ge
#print axioms ConvexApprox.IsChordalNet.exists_inner_ge
#check @ConvexApprox.IsChordalNet.exists_inner_ge_norm
#print axioms ConvexApprox.IsChordalNet.exists_inner_ge_norm
#check @ConvexApprox.IsChordalNet.exists_inner_pos
#print axioms ConvexApprox.IsChordalNet.exists_inner_pos
#check @ConvexApprox.IsChordalNet.separates_points
#print axioms ConvexApprox.IsChordalNet.separates_points
#check @ConvexApprox.IsChordalNet.eq_zero_of_inner_eq_zero
#print axioms ConvexApprox.IsChordalNet.eq_zero_of_inner_eq_zero
#check @ConvexApprox.IsChordalNet.nonempty
#print axioms ConvexApprox.IsChordalNet.nonempty
#check @ConvexApprox.IsChordalNet.two_le_card
#print axioms ConvexApprox.IsChordalNet.two_le_card
#check @ConvexApprox.IsChordalNet.span_eq_top
#print axioms ConvexApprox.IsChordalNet.span_eq_top
#check @ConvexApprox.BarrierData
#print axioms ConvexApprox.BarrierData
#check @ConvexApprox.BarrierData.error
#print axioms ConvexApprox.BarrierData.error
#check @ConvexApprox.BarrierData.tubeMargin
#print axioms ConvexApprox.BarrierData.tubeMargin
#check @ConvexApprox.BarrierData.openSet
#print axioms ConvexApprox.BarrierData.openSet
#check @ConvexApprox.BarrierData.closedSet
#print axioms ConvexApprox.BarrierData.closedSet
#check @ConvexApprox.BarrierData.error_nonneg
#print axioms ConvexApprox.BarrierData.error_nonneg
#check @ConvexApprox.BarrierData.tubeMargin_pos
#print axioms ConvexApprox.BarrierData.tubeMargin_pos
#check @ConvexApprox.exists_barrierData_error_lt
#print axioms ConvexApprox.exists_barrierData_error_lt
#check @ConvexApprox.chosenBarrierData
#print axioms ConvexApprox.chosenBarrierData
#check @ConvexApprox.chosenBarrierData_error_lt
#print axioms ConvexApprox.chosenBarrierData_error_lt
#check @ConvexApprox.nestedBarrierData
#print axioms ConvexApprox.nestedBarrierData
#check @ConvexApprox.nestedBarrierData_error_lt
#print axioms ConvexApprox.nestedBarrierData_error_lt
#check @ConvexApprox.nestedBarrierData_gap
#print axioms ConvexApprox.nestedBarrierData_gap
#check @ConvexApprox.nestedBarrierData_compactly_nested
#print axioms ConvexApprox.nestedBarrierData_compactly_nested
#check @ConvexApprox.nestedBarrierData_compact_closure
#print axioms ConvexApprox.nestedBarrierData_compact_closure
#check @ConvexApprox.nestedBarrierData_error_tendsto
#print axioms ConvexApprox.nestedBarrierData_error_tendsto
#check @ConvexApprox.nestedBarrierData_intersections
#print axioms ConvexApprox.nestedBarrierData_intersections
#check @ConvexApprox.BarrierData.hausdorff_error
#print axioms ConvexApprox.BarrierData.hausdorff_error
#check @ConvexApprox.nestedBarrierData_hausdorff_tendsto
#print axioms ConvexApprox.nestedBarrierData_hausdorff_tendsto
#check @ConvexApprox.exists_smooth_outer_approximation
#print axioms ConvexApprox.exists_smooth_outer_approximation
#check @ConvexApprox.outerErrorBound
#print axioms ConvexApprox.outerErrorBound
#check @ConvexApprox.outerErrorBound_nonneg
#print axioms ConvexApprox.outerErrorBound_nonneg
#check @ConvexApprox.infDist_le_outerErrorBound
#print axioms ConvexApprox.infDist_le_outerErrorBound
#check @ConvexApprox.outer_set_subset_tube
#print axioms ConvexApprox.outer_set_subset_tube
#check @ConvexApprox.hausdorffDist_le_outerErrorBound
#print axioms ConvexApprox.hausdorffDist_le_outerErrorBound
#check @ConvexApprox.outerErrorBound_le_simple
#print axioms ConvexApprox.outerErrorBound_le_simple
#check @ConvexApprox.infDist_le_exact_outer_error
#print axioms ConvexApprox.infDist_le_exact_outer_error
#check @ConvexApprox.hausdorffDist_le_exact_outer_error
#print axioms ConvexApprox.hausdorffDist_le_exact_outer_error
#check @ConvexApprox.singleton_norm_le_outer_error
#print axioms ConvexApprox.singleton_norm_le_outer_error
#check @ConvexApprox.chordalCos
#print axioms ConvexApprox.chordalCos
#check @ConvexApprox.chordalSin
#print axioms ConvexApprox.chordalSin
#check @ConvexApprox.chordalCos_pos
#print axioms ConvexApprox.chordalCos_pos
#check @ConvexApprox.chordal_sq_lt_two
#print axioms ConvexApprox.chordal_sq_lt_two
#check @ConvexApprox.unit_inner_eq_one_sub_half_sq
#print axioms ConvexApprox.unit_inner_eq_one_sub_half_sq
#check @ConvexApprox.chordalCos_le_inner
#print axioms ConvexApprox.chordalCos_le_inner
#check @ConvexApprox.unit_tangent_norm_sq
#print axioms ConvexApprox.unit_tangent_norm_sq
#check @ConvexApprox.chordalSin_nonneg
#print axioms ConvexApprox.chordalSin_nonneg
#check @ConvexApprox.chordalSin_sq
#print axioms ConvexApprox.chordalSin_sq
#check @ConvexApprox.unit_tangent_norm_le_chordalSin
#print axioms ConvexApprox.unit_tangent_norm_le_chordalSin
#check @ConvexApprox.chordalSin_le
#print axioms ConvexApprox.chordalSin_le
#check @ConvexApprox.support_displacement_le_chordalSin
#print axioms ConvexApprox.support_displacement_le_chordalSin
#check @ConvexApprox.local_outer_error
#print axioms ConvexApprox.local_outer_error
#check @ConvexApprox.directionalBarrier
#print axioms ConvexApprox.directionalBarrier
#check @ConvexApprox.directionalBarrier_le
#print axioms ConvexApprox.directionalBarrier_le
#check @ConvexApprox.directionalBarrier_halfspace
#print axioms ConvexApprox.directionalBarrier_halfspace
#check @ConvexApprox.directionalBarrier_tube
#print axioms ConvexApprox.directionalBarrier_tube
#check @ConvexApprox.directionalBarrier_eq_barrier
#print axioms ConvexApprox.directionalBarrier_eq_barrier
#check @ConvexApprox.contDiff_directionalBarrier
#print axioms ConvexApprox.contDiff_directionalBarrier
#check @ConvexApprox.convexOn_directionalBarrier
#print axioms ConvexApprox.convexOn_directionalBarrier
#check @ConvexApprox.strictConvexOn_directionalBarrier
#print axioms ConvexApprox.strictConvexOn_directionalBarrier
#check @ConvexApprox.directionalBarrier_lt_one_of_support
#print axioms ConvexApprox.directionalBarrier_lt_one_of_support
#check @ConvexApprox.exp_lower_directionalBarrier
#print axioms ConvexApprox.exp_lower_directionalBarrier
#check @ConvexApprox.directionalBarrier_sublevel_radius
#print axioms ConvexApprox.directionalBarrier_sublevel_radius
#check @ConvexApprox.tendsto_directionalBarrier_atTop
#print axioms ConvexApprox.tendsto_directionalBarrier_atTop
#check @ConvexApprox.isCompact_directionalBarrier_sublevel
#print axioms ConvexApprox.isCompact_directionalBarrier_sublevel
#check @ConvexApprox.cardinal_margin_iff
#print axioms ConvexApprox.cardinal_margin_iff
#check @ConvexApprox.inner_margin_pos
#print axioms ConvexApprox.inner_margin_pos
#check @ConvexApprox.inner_margin_cardinal_eq
#print axioms ConvexApprox.inner_margin_cardinal_eq
