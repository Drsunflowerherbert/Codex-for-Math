-- Give the short ID column and longer mathematical task columns useful widths.
function Table(table)
  local first = pandoc.utils.stringify(table.head.rows[1].cells[1].contents)
  if #table.colspecs == 4 then
    local widths = {0.18, 0.22, 0.22, 0.38}
    if first == "ID" then widths = {0.07, 0.37, 0.25, 0.31} end
    for i, width in ipairs(widths) do table.colspecs[i][2] = width end
  elseif #table.colspecs == 3 then
    local widths = {0.28, 0.36, 0.36}
    if first == "Example" then widths = {0.12, 0.14, 0.74} end
    for i, width in ipairs(widths) do table.colspecs[i][2] = width end
  end
  return table
end
