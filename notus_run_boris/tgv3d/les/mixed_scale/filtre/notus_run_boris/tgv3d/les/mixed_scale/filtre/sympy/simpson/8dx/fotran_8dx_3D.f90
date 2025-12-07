program simpson_3d
  implicit none
  
  ! 1) Déclaration des variables
  integer :: i, j, k, p, q, r
  real, dimension(-4:4, -4:4, -4:4) :: U
  real :: expr_discrete_3d, factor
  integer, dimension(-4:4) :: W
  
  ! 3) Poids Simpson 1D
  W(-4) = 1
  W(-3) = 4
  W(-2) = 2
  W(-1) = 4
  W(0) = 2
  W(1) = 4
  W(2) = 2
  W(3) = 4
  W(4) = 1
  
  ! 4) Facteur (dx/3)^3/(2dx)^3 = 1/13824
  factor = 1.0 / 13824.0
  
  ! Initialisation de l'expression (à remplacer par vos données réelles)
  expr_discrete_3d = 0.0
  
  ! Construction de l'approximation discrète (tensorisation Simpson)
  do p = -4, 4
    do q = -4, 4
      do r = -4, 4

      !  if ((i+p >= lbound(U,1) .and. i+p <= ubound(U,1)) .and. &
      !      (j+q >= lbound(U,2) .and. j+q <= ubound(U,2)) .and. &
      !      (k+r >= lbound(U,3) .and. k+r <= ubound(U,3))) then
          
          expr_discrete_3d = expr_discrete_3d + factor * W(p) * W(q) * W(r) * U(i+p, j+q, k+r)
      !  end if
      end do
    end do
  end do
  
  print *, "Expression discrète 3D :", expr_discrete_3d
  
end program simpson_3d
